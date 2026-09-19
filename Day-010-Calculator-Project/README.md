# Day 10 - Calculator Project

## What I Learned
- Functions with return values, storing output for reuse
- Functions returning multiple values
- Docstrings for documenting function purpose
- Recursion — used to restart the calculator without ending the program

## Project Overview
Console-based calculator supporting +, -, *, / — can continue calculating with the previous result or start fresh, until the user exits.

## How It Works
- Shows ASCII logo, takes first number, then operator, then second number.
- Performs the operation and shows the result.
- Asks whether to continue with the result, start over, or exit; loops accordingly.

## Code Highlights
- Dictionary mapping operators (`+`, `-`, `*`, `/`) to their functions
- Nested/recursive structure: main flow restarts calculation via recursion
- Input validation loop for continue/restart choice
- Functions taking parameters (`n1`, `n2`) and returning results for reuse
