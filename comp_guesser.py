import random

def comp_guesser(x):
    gen_number = int(input("Guess this number I choose: "))
    guessed_number = 0
    while guessed_number != gen_number:
        guessed_number = random.randint(1,x)
        if guessed_number == gen_number:
            print("You got it right!")
        if guessed_number > gen_number:
            print("You guessed higher")
        if guessed_number < gen_number:
            print("You guessed lower")