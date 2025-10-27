def infinite_chai():
    count = 1
    while True:
        yield f"Refill # {count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai() # Separate generator instance

for _ in range(5): # _ is used when we don't need to use this value, just to repeat 5 times, avoids creating unnecessary variable. Helps in linting
    print(next(refill))

for _ in range(6):
    print(next(user2)) # Separate state maintained

"""
Refill # 1
Refill # 2
Refill # 3
Refill # 4
Refill # 5
Refill # 1
Refill # 2
Refill # 3
Refill # 4
Refill # 5
Refill # 6
"""