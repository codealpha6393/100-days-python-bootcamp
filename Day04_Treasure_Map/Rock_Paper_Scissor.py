# Rock-Paper-Scissor Game

import random

# Define constants for Rock, Paper, and Scissor
ROCK = 0
PAPER = 1
SCISSOR = 2

# Define a dictionary to map the user's choice to the computer's choice and determine the winner
game_logic = {
    (ROCK, ROCK): "Game Draw!",
    (ROCK, PAPER): "Computer wins!",
    (ROCK, SCISSOR): "You win!",
    (PAPER, ROCK): "You win!",
    (PAPER, PAPER): "Game Draw!",
    (PAPER, SCISSOR): "Computer wins!",
    (SCISSOR, ROCK): "Computer wins!",
    (SCISSOR, PAPER): "You win!",
    (SCISSOR, SCISSOR): "Game Draw!"
}

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter Your Option 0-->Rock, 1-->Paper, 2-->Scissor: "))
            if user_choice < 0 or user_choice > 2:
                print("The number is invalid")
            else:
                return user_choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user_choice, computer_choice):
    return game_logic.get((user_choice, computer_choice), "Invalid input")

def play_game():
    print("Welcome to Rock-Paper-Scissor Game !--")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer_choice: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()