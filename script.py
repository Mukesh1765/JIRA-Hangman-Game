import csv
import os
import random

def get_random_country_names(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at path '{file_path}' was not found.")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Permission denied: cannot read file '{file_path}'.")
    
    country_names = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        country_names = [row[0] for row in reader]

    selected_countries = random.sample(country_names, k=10)
    if not selected_countries:
        raise ValueError("No countries found.")
    return selected_countries


def get_country_name(countries):
    if not countries:
        raise ValueError("No countries available.")
    return random.choice(countries)

class Hangman:
    def __init__(self):
        self.__country_name = get_country_name(get_random_country_names('./countries.csv'))
        self.__guessed_letters = set()
        self.__max_attempts = 5
        self.__attempts = 0

    def start_game(self):
        print("welcome to game", end = " ")
        print('''  
        _ _                                         
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                        |___/                       ''')
        print("you'll be guessing a country name.", end = "\n"); 
        print()
        print("Rules: 5 attempts, case-insensitive, no cheating!", end = "\n"); 
        print("Type your guess and press Enter. Let's begin!", end = "\n"); 
        print()

        # print(self.__country_name)

if __name__ == "__main__":
    game = Hangman()
    game.start_game()