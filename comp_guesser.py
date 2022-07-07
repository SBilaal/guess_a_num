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

def comp_guesser_v2(x):
    low = 1
    high = x

    # guess = 0
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        print(f"Max: {high} Min: {low} Guessed {guess}")
        print(f'I guessed: {guess}')
        feedback = input('Is my number too high(h), too low(l), or correct(c)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(feedback)
    print('You\'re correct!')
    
