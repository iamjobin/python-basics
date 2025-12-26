# Simple examples demonstrating Python comprehensions
"""
comprehensions.py

Simple examples demonstrating Python comprehensions (list, dict, set, nested).
Each example shows a normal loop-based approach(some) followed by the comprehension equivalent.
-> loop + condition + append → in one readable line

Guidelines:
- Prefer comprehensions for concise, readable transformations and filtering.
- Avoid very complex logic inside comprehensions; use a loop for clarity.
"""

# Normal approach using for loop
squares = []
for i in range(1, 6):
    squares.append(i * i)

print(squares)

# 1. List
squares_compre = [i * i for i in range(1,6)]
print(squares_compre)

# condition
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)

# data transform
messages = ['  hi  ', 'hello  ', '  bye']
cleaned = [msg.strip().upper() for msg in messages]
print(cleaned)


# 2. Dict
names = ['Virat', 'Rohit', 'Rahul']
length_json = {name: len(name) for name in names}
print(length_json)

# Filtering
scores = {
    'a':10,
    'b':20,
    'c':15
}
passed = {k:v for k,v in scores.items() if v>10}
print(passed)


# 3. Set
nums = [1, 2, 2, 3, 3, 3]
unique_sqrs = {i * i for i in nums}
print(unique_sqrs)


# 4.Nested
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)


# Exercise
users = [
    {"name": "Jobin", "active": True},
    {"name": "Alex", "active": False},
    {"name": "Rohan", "active": True}
]
'''
1. Extract active user names
2. Convert names to uppercase
3. Store result as list
'''

active_users = [item['name'].upper() for item in users if item['active']]
print(active_users)
