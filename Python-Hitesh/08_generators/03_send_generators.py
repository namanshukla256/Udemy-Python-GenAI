def chai_customer():
    print("Welcome : What chai would you like?")
    order = yield # Initial yield to start the generator
    while True:
        print(f"Preparing: {order}")
        order = yield # Yield to receive the next order

stall = chai_customer()
next(stall)  # Prime the generator to the first yield. Start the generator

stall.send("Masala Chai")
stall.send("Ginger Chai")

"""
Welcome : What chai would you like?
Preparing: Masala Chai
"""
