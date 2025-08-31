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

print(get_country_name(get_random_country_names('./countries.csv')))