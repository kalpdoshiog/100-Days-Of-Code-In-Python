# Day 14 - Higher Lower Game

## What I Learned
- Breaking a game into small reusable functions with docstrings
- Pulling fields out of a list of dictionaries imported from another file (`game_data`)
- Carrying state between rounds (B becomes the next A)

## Project Overview
Console game comparing the follower counts of two public figures. Guess who has more, and keep going until you get one wrong.

## How It Works
- Shows two random accounts (name, description, country) and asks for 'A' or 'B'.
- Correct guess: score goes up, account B becomes account A, and a new B is picked.
- Wrong guess: final score is shown and the game ends.

## Code Highlights
- `format_data()` turns an account dictionary into a printable line
- `check_answers()` compares follower counts and returns whether the guess was right
- `while` loop with a `game_should_continue` flag controlling the game
