import csv
import os
import random
import sys

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
        try:
            self.__country_name = self.__get_country_name(self.__get_random_country_names('./countries.csv')).lower()
            self.__guessed_letters = set()
            self.__max_attempts = 5
            self.__char_array = ['_' if char != ' ' else ' ' for char in self.__country_name]
            self.__attempts = 0
        except (FileNotFoundError, PermissionError, ValueError, csv.Error) as e:
            print(f"Initialization Error: {e}")
            print("The game cannot start. Please ensure 'countries.csv' exists and is accessible.")
            sys.exit(1) 
        except Exception as e:
            print(f"An unexpected error occurred during initialization: {e}")
            sys.exit(1)

    def start_game(self):
        """Starts the Hangman game, displaying the welcome message and rules."""
        print("Welcome to Hangman!")
        print(r'''  
_ _                                         
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
        print("You'll be guessing a country name.")
        print()
        print("Rules: 5 attempts, case-insensitive, no cheating!", end="\n")
        print("Type your guess and press Enter. Let's begin!", end="\n")
        print()
        print("You can guess until the hangman drawing is complete.")
        print("Initial condition:")
        print(self.hangman_symbols[0])
        print("If you reach the last stage, you lose!")
        print("Last stage:")
        print(self.hangman_symbols[-1])
        print()
        print()

        try:
            self.__game_logic()
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user. Thanks for playing!")
        except Exception as e:
            print(f"\nAn unexpected error occurred during gameplay: {e}")
            print("The game will now exit.")

    def __game_logic(self):
        """Contains the core game loop and logic."""
        print("Let's start the game!")
        country_len = len(self.__country_name) - self.__country_name.count(' ')
        print(f"The country name has {country_len} letters.")
        print()
        print(' '.join(self.__char_array))

        country_name_list = list(self.__country_name)

        while self.__char_array != country_name_list and self.__attempts < self.__max_attempts:
            try:
                guess = input("Enter a Letter: ").lower()
                if guess.isspace():
                    raise ValueError("Please enter a letter, not a space.")
                
                guess = guess.strip()
                
                if len(guess) != 1:
                    raise ValueError("Please enter exactly one character.")
                if not guess.isalpha():
                    raise ValueError("Please enter a letter (a-z).")

                if guess in self.__guessed_letters:
                    print("You've already guessed that letter.")
                    print()
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

                print("Current state: ")
                print(self.hangman_symbols[self.__attempts])
                print(f"Attempts left: {self.__max_attempts - self.__attempts}")
                print(" ".join(self.__char_array))
                print(f"Guessed letters: {', '.join(sorted(self.__guessed_letters))}")
                print()

            except ValueError as ve:
                print(f"Invalid input: {ve}")
                print()
            except Exception as e:
                print(f"An error occurred processing your guess: {e}")
                print()

        print("Game Over!")
        if self.__char_array == country_name_list:
            print("Congratulations! You've guessed the country name correctly!")
            calculate_score = int((self.__max_attempts - self.__attempts) / self.__max_attempts * 100)
            print("your score is: ", calculate_score)
        else:
            print("Sorry, you've run out of attempts.")
        print(f"The country was: {self.__country_name}")

    @staticmethod
    def __get_random_country_names(file_path):
        """
        Reads a CSV file and returns a list of 10 random country names.
        Assumes the country name is in the first column and the first row is a header.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at path '{file_path}' was not found.")
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Permission denied: cannot read file '{file_path}'.")

        country_names = []
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  
                country_names = [row[0] for row in reader if row]

            if not country_names:
                raise ValueError("The CSV file contains no country data after the header.")

            selected_countries = random.sample(country_names, k=min(10, len(country_names)))
            return selected_countries

        except csv.Error as e:
            raise csv.Error(f"Error reading CSV file: {e}")
        except UnicodeDecodeError:
            raise ValueError("File encoding error. Please ensure the CSV file uses UTF-8 encoding.")

    @staticmethod
    def __get_country_name(countries):
        """Selects a random country from the provided list."""
        if not countries:
            raise ValueError("No countries available to choose from.")
        return random.choice(countries)

if __name__ == "__main__":
    try:
        game = Hangman()
        game.start_game()
    except Exception as e:
        print(f"A critical error occurred: {e}")
        sys.exit(1)