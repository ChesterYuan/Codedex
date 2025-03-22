from math import pi
from random import choice

# Planet data dictionary with radii in km
planet_data = {
    'Mercury': 2440,
    'Venus': 6052,
    'Earth': 6371,
    'Mars': 3390,
    'Saturn': 58232,
    'Jupiter': 69911,
    'Uranus': 25362,
    'Neptune': 24622
}

# Get a random planet name from the dictionary keys
planets = list(planet_data.keys())
random_planet = choice(planets)

# Get the radius for the selected planet
r = planet_data[random_planet]

# Calculate surface area using 4πr²
area = round(4 * pi * r ** 2, 2)

print(f'{random_planet} has a surface area of {area} sq km')
