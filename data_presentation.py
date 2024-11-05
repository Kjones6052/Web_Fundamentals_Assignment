# Task 3: Data Presentation and Analysis
# Perform a simple analysis, such as finding the planet with the longest orbit period or the heaviest 
# planet. 
import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets_data = response.json()['bodies']
    planets = []

    #process each planet info
    for planet in planets_data:
        if planet['isPlanet']:
            name = planet['englishName'] #get planet English name
            mass = int(planet['mass']['massValue']) #get planet mass
            orbit_period = planet['sideralOrbit'] #get planet orbit period
            planets.append({"Planet": name, "Mass": mass, "Orbit Period": orbit_period})
    
    return planets
    

def get_heaviest_planet():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets_data = response.json()['bodies']
    mass_values = []
    for planet in planets_data:
        if planet['isPlanet']:
            mass = planet['mass']['massValue']
            mass_values.append(mass)
    max_mass = max(mass_values)
    for planet in planets_data:
        if planet['isPlanet']:
            if planet['mass']['massValue'] == max_mass:
                return f"The heaviest planet is {planet['englishName']} with a mass of {max_mass}kg."        


planets = fetch_planet_data()
print(planets)
heaviest_planet = get_heaviest_planet()
print(heaviest_planet)