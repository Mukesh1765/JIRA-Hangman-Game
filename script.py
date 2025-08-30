import csv
import random

def get_random_country_names(file_path):
    country_names = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        country_names = [row[0] for row in reader]
        country_names.pop(0)

    selected_countries = []
    for _ in range(10):
        random_index = random.randint(0, len(country_names) - 1)
        country_name = country_names[random_index]
        selected_countries.append(country_name)

    return selected_countries

print(get_random_country_names('./countries.csv'))