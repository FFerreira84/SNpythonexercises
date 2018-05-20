import random

while True:
    random_num = random.randint(0,2)
    print random_num
    again = raw_input("Would you like to continue this game? (yes/no) ")
    if again == "no":
        break