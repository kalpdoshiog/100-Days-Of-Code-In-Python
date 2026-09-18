# Day 8 - Caesar Cipher Project

## What I Learned
- Functions with parameters, passing dynamic values instead of fixed ones
- Positional arguments (order-dependent) vs keyword arguments (name-dependent)
- Using the modulo operator to wrap letter shifts around the alphabet

## Project Overview
Encrypts or decrypts a message by shifting each letter forward or backward in the alphabet by a user-specified amount.

## How It Works
- User provides direction (encode/decode), shift amount, and the text.
- "Encode" shifts letters forward, "decode" shifts backward.
- Program loops, prompting to continue or exit after each run.

## Code Highlights
- `index()` to locate a letter's position in the alphabet
- Positional and keyword arguments for function flexibility
- Modulo operator to cycle shifts past the alphabet's end
