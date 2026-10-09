# Day 12 - Number Guessing Game

## What I Learned
- Local scope — variables inside a function are only visible there
- Global scope — variables at the top level, accessible everywhere
- Python has no block scope — a variable in a loop/if/while isn't isolated unless it's inside a function
- `global` keyword to modify a global variable from within a function
- Naming convention for global constants (`ALL_CAPS_WITH_UNDERSCORES`)

## Project Overview
Console game where the player guesses a number between 1 and 100, with attempts limited by chosen difficulty (easy/hard).

## How It Works
- Picks a random number, asks for difficulty, sets attempts accordingly (easy: 10, hard: 5).
- Each guess gets feedback — too high, too low, or correct — and decrements remaining attempts.
- Game ends on a correct guess or when attempts run out.

## Code Highlights
- `attempts()` function using `global attempt` to set remaining tries based on difficulty
- While loop driving the guess-feedback cycle until win or loss
