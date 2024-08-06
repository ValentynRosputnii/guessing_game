from random import randint
from art import logo, win_logo, lose_logo

def set_difficulty():
    game_lvl = {
    "easy": 10,
    "medium": 7,
    "hard": 5
    }

    lvl = input("Choose a difficulty. Type 'easy', 'medium', 'hard': ")
    palyer_lives = game_lvl[lvl]
    
    return palyer_lives

def check_answer(player_number, answer, player_lives):
    if player_number < answer:
        player_lives -= 1
        print(f"\nGuessed number is greater than {player_number}.\nTry again.\nLives: {player_lives}\n")
    elif player_number > answer:
        player_lives -= 1
        print(f"\nGuessed number is lower than {player_number}.\nTry again.\nLives: {player_lives}\n")
    else:
        print(f"\nYou got it! The answer was {answer}.\n")
        print(win_logo)
    
    return player_lives

def guessing_game():
    print(logo)
    print("Welcome to the Guessing Game! \nI'm thinking of a number between 1 and 100.")
    
    player_lives = set_difficulty()

    answer = randint(1, 100)

    while player_lives > 0:
        player_number = int(input("The number that is being guessed is: "))
        player_lives = check_answer(player_number, answer, player_lives)

    if player_lives == 0:
        print(lose_logo)

guessing_game()