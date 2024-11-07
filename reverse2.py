from concurrent.futures import ThreadPoolExecutor

def reverse_number_part(part):
    return part[::-1]

def split_and_reverse(number, n):
    number_str = str(number)
    part_size = len(number_str) // n
    parts = [number_str[i:i + part_size] for i in range(0, len(number_str), part_size)]
    
    with ThreadPoolExecutor(max_workers=n) as executor:
        reversed_parts = list(executor.map(reverse_number_part, parts))
    
    reversed_number = int("".join(reversed_parts[::-1]))
    return reversed_number

# Przykład użycia
print(split_and_reverse(123456789, 3))  # Wynik: 987654321
