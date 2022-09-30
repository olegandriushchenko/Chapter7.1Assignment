import random

random.randrange(0, 50, 25)

number_to_guess = random
user_input = input("Guess the number from 0 to 50\n")
    if user_input > number_to_guess:
        print("The value is too low")
    elif user_input < number_to_guess:
        print("The value is too high")
    elif user_input == number_to_guess:
        print("You guessed correctly!")





