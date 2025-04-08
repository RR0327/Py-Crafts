"""import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number within the range!")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("That's not a valid number. Please try again.")

if __name__ == "__main__":
    guessing_game()"""


import random

def guess_num():
    print("Welcome to the game of number guessing.")
    num_to_guess = random.randint(1, 10)

    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number within the range!")

            elif guess < num_to_guess:
                print("Too low! Try again.")

            elif guess > num_to_guess:
                print("Too high! Try again.")

            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {num_to_guess} in {attempts} attempts.")

        except ValueError:
            print("That's not a valid number. Please try again.")

if __name__ == "__main__":
    guess_num()

