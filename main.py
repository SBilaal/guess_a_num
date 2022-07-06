import random
import comp_guesser, user_guesser

def main():
    selected_choice = input("Type 1 to select user guessing mode, and 2 for AI guessing mode: ")
    while True:
        if selected_choice == "1":
            user_guesser.user_guesser(20)
            break
        elif selected_choice == "2":
            comp_guesser.comp_guesser(20)
            break
        else:
            print("Invalid selection")

if __name__ == '__main__':
    main()