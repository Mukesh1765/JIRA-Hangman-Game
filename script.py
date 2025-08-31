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
        self.__char_array = [char if char == ' ' else '_' for char in self.__country_name]
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
        self.__game_logic()


    def __game_logic(self):
        print("Lets start the game!")
        country_len = len(self.__country_name) - self.__country_name.count(' ')
        print(f"The country name has {country_len} letters.")
        print()
        print(' '.join(self.__char_array))
        country_name_list = [char for char in self.__country_name]

        while self.__char_array != country_name_list and self.__attempts < self.__max_attempts:
            guess = input("Enter a Letter: ").lower()
            # if len(guess) != 1 or not guess.isalpha():
            #     print("Invalid input. Please enter a single letter.")
            #     continue

            if guess in self.__guessed_letters:
                print("You've already guessed that letter.")
                continue

            self.__guessed_letters.add(guess)

            if guess in self.__country_name:
                print("Good guess!")
                for i, letter in enumerate(self.__country_name):
                    if letter == guess:
                        self.__char_array[i] = guess
            else:
                print("Wrong guess.")
                self.__attempts += 1

            print("current state: ")
            print(self.hangman_symbols[self.__attempts])
            print(f"Attempts left: {self.__max_attempts - self.__attempts}")
            print(" ".join(self.__char_array))
            print()

        print("Game Over!")
        if self.__char_array == country_name_list:
            print("Congratulations! You've guessed the country name correctly!")
        else:
            print("Sorry, you've run out of attempts.")
        print(f"The country was: {self.__country_name}")

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