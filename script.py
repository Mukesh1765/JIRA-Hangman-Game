import csv
import os
import random

class Hangman:
    hangman_symbols = [r"""
   +--+
   |  |
      |
      |
      |
      |
  =====""",
    r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
    r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
    r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
    r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
    r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
  ====="""]

    def __init__(self):
        self.__country_name = self.__get_country_name(self.__get_random_country_names('./countries.csv')).lower()
        self.__guessed_letters = set()
        self.__max_attempts = 5
        self.__char_array = ['_' for _ in self.__country_name]
        self.__attempts = 0

    def start_game(self):
        print("welcome to game")
        print(r'''  
_ _                                         
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
        print("you'll be guessing a country name.")
        print()
        print("Rules: 5 attempts, case-insensitive, no cheating!", end = "\n"); 
        print("Type your guess and press Enter. Let's begin!", end = "\n"); 
        print()
        print("you can guess until man body complete")
        print("initial_condition : ")
        print(self.hangman_symbols[0])

        print("if you reach the last stage, you lose!")
        print("last stage:")
        print(self.hangman_symbols[-1])

        print()
        print()

        print("Lets start the game!")
        print(f"The country name has {len(self.__country_name)} letters.")
        print()

        self.__game_logic()


    def __game_logic(self):
        print(" ".join(self.__char_array))

    @staticmethod
    def __get_random_country_names(file_path):
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

    @staticmethod
    def __get_country_name(countries):
        if not countries:
            raise ValueError("No countries available.")
        return random.choice(countries)

if __name__ == "__main__":
    game = Hangman()
    game.start_game()