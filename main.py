import random

def guess(x, guessed_number):
    if x == guessed_number:
        print("You got it right!")
        return True
    if x > guessed_number:
        print("You guessed higher")
        return False
    if x < guessed_number:
        print("You guessed lower")
        return False

def main():
    is_correct = False
    guessed_number = random.randint(0,10)
    while not is_correct:
        is_correct = guess(int(input("Guess the number chosen: ")), guessed_number)

if __name__ == '__main__':
    main()