# Task 3: Analyzing and Displaying Data

import requests
import json

# 1. Modify the script to fetch data for three different Pokémon.
def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}') # Fetching data from the Pokemon API
    json_data = response.text # Putting JSON text from API into a variable
    pokemon_data = json.loads(json_data) # Converting JSON to Python Object (Dictionary)
    name = pokemon_data["name"]
    abilities = pokemon_data["abilities"]
    return name, abilities

# 2. Create a function to calculate and return the average weight of these Pokémon.
def calculate_avg_weight(pokemon_list):
    weight_list = []
    for pokemon in pokemon_list:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}') # Fetching data from the Pokemon API
        json_data = response.text # Putting JSON text from API into a variable
        pokemon_data = json.loads(json_data) # Converting JSON to Python Object (Dictionary)
        weight = pokemon_data["weight"]
        weight_list.append(weight)
    avg_weight = (sum(weight_list)) / (len(weight_list))
    return avg_weight

# 3. Print the names, abilities, and average weight of the three Pokémon.
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
for name in pokemon_names:
    pokemon_info = fetch_pokemon_data(name)
    print(pokemon_info)
avg_weight = calculate_avg_weight(pokemon_names)
print(avg_weight)