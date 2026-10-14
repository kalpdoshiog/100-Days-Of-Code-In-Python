# Display art
from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns data into printable format """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from  {account_country}"

def check_answers(user_guess, a_followers, b_followers):
    """Take the user guess and the followers counts and returns if they got it right or not."""
    # Check if user is correct.
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0

# Generate random account from game data
account_b = random.choice(data)

game_should_continue = True

while game_should_continue:

    # Making the account at potion B becomes the next account at potion A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user for guess.

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count from each account.

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Use if to check user is correct

    is_correct = check_answers(user_guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

    # Give feedback to user.

    if is_correct:
        # tack score.
        score += 1
        print(f"You're Right. Current score {score}")

    else:
        print(f"Sorry, that wrong. Final score: {score}")
        game_should_continue = False
