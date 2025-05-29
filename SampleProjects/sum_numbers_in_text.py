import re

def sum_numbers_in_text(text):
    numbers = re.findall(r'\b\d+\b', text)
    
    return sum(int(num) for num in numbers)

print(sum_numbers_in_text("Hello 123 world 456"))
