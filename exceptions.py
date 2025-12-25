import logging
# x = int('Hello') #it throws a nvalid literal for int() ValueError

try:
    x = int('Hello')
except ValueError:
    print('Invalid Number')

# Multi Exception Block
try:
    x = int(input())
    y = 10/x
except ValueError:
    print('Not a Number')
except ZeroDivisionError:
    print('Division by zero')

# else & finally
try:
    x = int('10')
except ValueError as e:
    print(e)
else:
    print('Success')
finally:
    print('Finally Block invoked(Always)')


#Throw/Raise Exceptions
def validateAge(age: int):
    if age < 18:
        raise ValueError('Under Age')
    print('Accepted Age')


validateAge(int(input()))

# Custom Exceptions
class ToolError(RuntimeError):
    pass

raise ToolError("Tool failed")

# Re Raising Exceptions
try:
    x = 10/0
except Exception:
    print('Error log')
    raise

try:
    int("abc")
except ValueError as e:
    logging.exception(e)
    raise RuntimeError("Parsing failed") from e
