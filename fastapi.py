from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import httpx

app = FastAPI()

usery = []


class User(BaseModel):
    id: int
    name: str
    email: str


@app.post("/users/")
def create_user(user: User):
    usery.append(user)
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in usery:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/slow")
async def slow_endpoint():
    time.sleep(3)
    return {"message": "This took too long!"}


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app.get("/parallel")
async def parallel_requests():
    urls = ["https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2"]
    results = []
    for url in urls:
        results.append(await fetch_url(url))
    return results
