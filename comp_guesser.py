import random

def comp_guesser(x):
    gen_number = int(input("Guess this number I choose: "))
    guessed_number = 0
    lower = 1
    higher = x

    while guessed_number != gen_number:
        guessed_number = random.randint(lower,higher)
        print(f"Max: {higher} Min: {lower} Guessed {guessed_number}")
        if guessed_number == gen_number:
            print("You got it right!")
        if guessed_number > gen_number:
            higher = guessed_number
            print("You guessed higher")
        if guessed_number < gen_number:
            lower = guessed_number
            print("You guessed lower")