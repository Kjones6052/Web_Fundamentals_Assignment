# 2. Exploring the Digital Cosmos with Python and the Web
# Problem Statement: 
# Imagine you are a developer tasked with creating a feature for a web application that provides users with insightful information about various 
# space objects. Your application will fetch data from a publicly available space API, process this data, and display it in a user-friendly format.

# Task 1: Set up a Python Virtual Environment and Install Required Packages
# Create a new virtual environment in Python. Activate the virtual environment. Install the `requests` package for making HTTP requests.

# Task 2: Fetch Data from a Space API 
# Write a Python script that makes a GET request to a space API 
# (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.
# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName'] #get planet English name
            mass = planet['mass']['massValue'] #get planet mass
            orbit_period = planet['sideralOrbit'] #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
