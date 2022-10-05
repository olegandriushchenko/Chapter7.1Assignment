import random

random_number = random.randrange(0, 50)

attemts = 7

number_to_guess = random

while attemts > 0:
    user_input = input("Guess the number from 0 to 50\n")
    user_input = int(user_input)

    if user_input > number_to_guess:
        print("The value is too low")
        attemts -= 1
    elif user_input < number_to_guess:
        print("The value is too high")
        attemts -= 1
    elif user_input == number_to_guess:
        print("You guessed correctly!")

if attemts == 0:
    print("No more attemts")





