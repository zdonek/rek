from concurrent.futures import ThreadPoolExecutor, as_completed

def reverse_number_part(part):
    return part[::-1]

def split_and_reverse(number, n):
    number_str = str(number)
    part_size = len(number_str) // n
    parts = [number_str[i:i + part_size] for i in range(0, len(number_str), part_size)]
    
    reversed_parts = []
    with ThreadPoolExecutor(max_workers=n) as executor:
        futures = [executor.submit(reverse_number_part, part) for parts in part]
        for future in as_completed(futures):
            reversed_parts.append(future.result())
    
    reversed_number = int("".join(reversed_parts))
    return reversed_number

# Przykład użycia
print(split_and_reverse(123456789, 3))
