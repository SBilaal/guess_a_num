import random

def guess(x):
    gen_number = random.randint(0,x)
    guessed_number = int(input("Guess the number chosen: "))
    while guessed_number != gen_number:
        if guessed_number == gen_number:
            print("You got it right!")
        if guessed_number > gen_number:
            print("You guessed higher")
        if guessed_number < gen_number:
            print("You guessed lower")

def main():
    guess(20)
if __name__ == '__main__':
    main()