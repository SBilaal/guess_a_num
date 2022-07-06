import random

def user_guesser(x):
    gen_number = random.randint(1,x)
    guessed_number = 0
    while guessed_number != gen_number:
        guessed_number = int(input("Guess the number chosen: "))
        if guessed_number == gen_number:
            print("You got it right!")
        if guessed_number > gen_number:
            print("You guessed higher")
        if guessed_number < gen_number:
            print("You guessed lower")