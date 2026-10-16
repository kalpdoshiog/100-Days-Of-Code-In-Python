# Day 15 - Coffee Machine Project

## What I Learned
- Nested dictionaries for storing menu data (ingredients, cost) and machine resources
- Splitting a program into single-purpose functions with docstrings
- Updating shared state (resources, money) across functions
- Combining dictionaries, functions, conditionals, loops, and arithmetic in one project

## Project Overview
Console coffee vending machine. The user picks a drink, inserts coins, and gets the coffee if the machine has enough ingredients and the payment covers the cost.

## How It Works
- Choose espresso, latte, or cappuccino. Type `report` to see resources and money, or `off` to shut the machine down.
- The machine checks there are enough water, milk, and coffee before continuing.
- It asks for quarters, dimes, nickels, and pennies and totals the coins.
- Not enough money: the user is refunded. Too much money: change is returned.
- On success, ingredients are deducted and the money is added to the machine's total.

## Code Highlights
- `sufficient_resources()` checks ingredients before taking any payment
- `calculate_coins()` converts inserted coins into a dollar total
- `enough_money_received()` handles refund, exact payment, and change
- `make_coffee()` deducts ingredients after a successful sale
- Running profit tracked and shown in the report
