from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")

random_num = random.randint(1, 100)
# print(f"Pssst 😉, the guessing number is {random_num} do not tell anyone🤫")

difficulty = input("Choose a difficulty: Type 'easy' or 'hard' : ").lower()

play_game = True
attempt = 0
def attempts():
    global attempt
    if difficulty == "easy":
        attempt = 10
        print(f"You have {attempt} attempts remaining to guess the number. ")
    elif difficulty == "hard":
        attempt = 5
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        print("You press wrong difficulty please restart game again.")

attempts()

while play_game:

    if attempt == 0:
        print("You've run out of guesses. You Lose")
        break

    make_guess = int(input("Make a guess: "))

    if make_guess == random_num:
        print(f"You got it! The answer was {random_num}.")
        break
    elif make_guess > random_num:
        print("Too High. \nGuess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number. ")
    elif make_guess < random_num:
        print("Too Low. \nGuess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number. ")
