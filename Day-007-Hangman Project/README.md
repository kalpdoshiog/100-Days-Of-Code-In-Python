# Day 7 - Hangman Project

## What I Learned
- Combining loops, functions, conditionals, and string manipulation into one project
- Using a `for` loop inside a `while` loop while preserving previously updated data

## Project Overview
Word-guessing game where the player guesses a randomly chosen word one letter at a time, with 6 lives before losing.

## How It Works
- Program picks a random word and tracks it as a list of underscores (unguessed) alongside the actual letters.
- Correct guesses reveal the letter in the displayed word; incorrect guesses cost a life.
- Game ends in a win (word fully guessed) or a loss (all 6 lives used).

## Code Highlights
- Real-time tracking and updating of the displayed word
- Lives counter limiting incorrect guesses
