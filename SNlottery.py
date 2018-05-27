import random

def lotterygame():
    lottery = []
    numbers = int(raw_input("Insert the amount of numbers to generate: "))
    while len(lottery) < numbers:
        a = random.randint(1,50)
        if a not in lottery:
            lottery.append(a)
    print  "Your numbers are:\n" + str(sorted(lottery))
lotterygame()