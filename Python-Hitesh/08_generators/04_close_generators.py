def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(f"Serving {chai}")

def chai_stall():
    try:
        while True:
            order = yield "Waiting for order..."
    except:
        print("Stall closed, No more orders can be taken.")

stall = chai_stall()
print(next(stall))  # Start the generator
stall.close()  # Close the generator. Cleans up resources


"""
Serving Matcha
Serving Oolong
Waiting for order...
Stall closed, No more orders can be taken.
"""
