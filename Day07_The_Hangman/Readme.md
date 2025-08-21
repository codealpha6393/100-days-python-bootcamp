# Hangman Game

A classic word-guessing game implemented in Python. This is my solution for **Day 7** of Dr. Angela Yu's [**100 Days of Code: The Complete Python Pro Bootcamp**](https://www.udemy.com/course/100-days-of-code/).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [What I Learned](#what-i-learned)
- [How to Run](#how-to-run)

## Overview

This is a terminal-based implementation of the classic Hangman game. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time. The player has a limited number of lives (incorrect guesses) before the game is over.

This project was a fantastic exercise in core Python programming concepts, including control flow, loops, functions, and string manipulation.

## Features

- **Random Word Selection:** The game picks a word at random from a custom list.
- **ASCII Art:** Visual feedback for each stage of the hangman, providing a classic game feel.
- **Lives Counter:** Tracks and displays the number of remaining lives.
- **Input Validation:** Handles invalid inputs (e.g., multiple characters, already guessed letters).
- **User-Friendly Display:** Clearly shows the current state of the word, guessed letters, and remaining lives.

## How to Play

1.  The game will randomly choose a word.
2.  You will see a series of underscores (`_ `), each representing a letter in the word.
3.  Guess one letter at a time.
4.  If the letter is in the word, it will be revealed in its correct position(s).
5.  If the letter is not in the word, you lose a life and a part of the hangman is drawn.
6.  The game continues until you either:
    -   Guess the entire word correctly (You Win!), or
    -   Run out of lives (You Lose!).

## Project Structure

The main logic of the game is contained within a single Python file:
hangman/
│
├── hangman.py # The main game script
├── words.py # Module containing the list of words (optional)
└── README.md # This file


## What I Learned / Key Concepts Practiced

This project was an excellent way to solidify my understanding of several fundamental Python concepts:

-   **Control Flow:** Extensive use of `if/else` statements to check guesses and manage game state.
-   **Loops:** Using `while` loops to keep the game running until a win or loss condition is met.
-   **Functions:** Breaking down the game logic into reusable functions (e.g., `check_guess()`, `get_guess()`).
-   **Strings and Lists:** Manipulating data structures to display the current progress (e.g., converting a string to a list of characters and back).
-   **Random Module:** Using `random.choice()` to select a random word from a list.
-   **Input Handling:** Validating user input to ensure it's a single alphabetic character that hasn't been guessed before.

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone or download this project to your local machine.
3.  Navigate to the project directory in your terminal or command prompt.
4.  Run the game using the following command:

```bash
python hangman.py
