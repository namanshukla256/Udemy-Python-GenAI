def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"

stall = serve_chai()

for cup in stall:
    print(f"Serving {cup}")

"""
Serving Cup 1: Masala Chai
Serving Cup 2: Ginger Chai
Serving Cup 3: Cardamom Chai
"""

# Normal function
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai)  # <generator object get_chai_gen at 0x7f8b8c0d4d30>
print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
# print(next(chai))  # StopIteration Error