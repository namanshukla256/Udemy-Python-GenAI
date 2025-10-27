from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied. Admins only.")
            return None # Early return if not admin
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Accessing the tea inventory...")

access_tea_inventory("guest")  # Access denied. Admins only.
access_tea_inventory("admin")  # Accessing the tea inventory...