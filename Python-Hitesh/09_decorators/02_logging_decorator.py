from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type_of_chai, milk="no"):
    print(f"Brewing a cup of {type_of_chai} chai and milk status {milk}")

brew_chai("Masala")

"""
Calling: brew_chai
Brewing a cup of Masala chai and milk status no
Finished: brew_chai
"""