from functools import wraps
# wraps is used to preserve the original function's metadata

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def greet():
    print("Hello there!")

greet()
print(greet.__name__)  # Output: greet

"""
Something is happening before the function is called.
Hello there!
Something is happening after the function is called.
"""