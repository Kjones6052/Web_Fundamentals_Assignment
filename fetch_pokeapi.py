# Task 2: Fetching Data from the Pokémon API
# 1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).
# 2. Extract and print the name and abilities of the Pokémon.
import requests
import json

# Fetching data from the Pokemon API
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

# Converting JSON to Python Object (Dictionary)
pikachu_data = json.loads(json_data)

# Printing data
print(pikachu_data["name"]) 
print(pikachu_data["abilities"]) 
