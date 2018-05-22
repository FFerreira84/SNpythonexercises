import random

def main():
    secret = random.randint(1, 10)
    guess = 0

    while True:
        guess = int(raw_input("Guess the secret number between 1 and 10: "))
        if secret == guess:
            print "You guessed correctly!"
            break
        elif guess > secret:
            print "Try a lower number."
        else:
            print "Try a higher number."

if __name__ == "__main__":
    main()