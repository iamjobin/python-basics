"""
args.py

Simple demonstrations of Python argument unpacking and call patterns.

- `*args` collects positional arguments into a tuple.
- `**kwargs` (or `**params`) collects keyword arguments into a dict.

This file shows small helper functions and example calls. Only documentation
and inline comments were added; no runtime logic was modified.
"""

# Sum any number of positional arguments collected via `*args`.
def add_all(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(add_all(1,2,6))

# Accepts user information as keyword arguments and prints the `name` field.
def print_user(**user):
    print(user['name'])

print_user(name='jobin', age=23)

# Demonstrates capturing positional (`args`) and keyword (`kwargs`) arguments.
def tool(*args, **kwargs):
    print(args)
    print(kwargs)

tool(1, 2, a=10, b=20)

# Named tool runner: `name` is typed, additional params are captured in `**params`.
def run_tool(name: str, **params):
    print(f'Running {name} with {params}')

run_tool('search', query='py', limit=5)

# Examples of argument unpacking from sequences and mappings.
nums = [1, 2, 3, 4, 5]
print(add_all(*nums))

data = {'name': 'jobin', 'role': 'dev'}
print_user(**data)
