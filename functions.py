def greet():
    print('Hello World!')


def greet(name):
    print(f'Hello {name}')


def greet(name: str = 'World!'):
    print(f'Hello {name}')

# There is no fun overloading concept in py, so latest one stays/overrides
greet()
greet('Jobin')
