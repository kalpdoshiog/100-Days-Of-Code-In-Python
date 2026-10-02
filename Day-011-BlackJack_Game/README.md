# Day 11 - Blackjack Game Project

## What I Learned
- Capstone project tying together functions, conditionals, loops, and game logic learned so far
- Structuring game state and round-by-round flow with while loops
- Ace-as-1-or-11 scoring logic and blackjack detection

## Project Overview
Console-based Blackjack: user vs. computer dealer, with hit/pass decisions, dealer auto-draw below 17, and replay support.

## How It Works
- Deals 2 cards each to start; player chooses to draw or pass.
- Dealer draws until its score hits 17+.
- Score checks handle blackjack (score 0), bust (>21), and ace downgrade (11→1) when over 21.
- Result compared and shown; player can restart for a new round.

## Code Highlights
- `deal_card()`, `calculate_score()`, `compare()` as separate functions with docstrings
- `calculate_score()` auto-converts an ace from 11 to 1 when the hand busts
- Game loop restarts cleanly via a `start_again` flag rather than breaking the program
  
