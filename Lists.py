planets = ['Mercur', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1])
print(planets[2:5])
print(planets[-1])

planets[3] = 'Malacandra'
print(planets)

print(len(planets))


# Sorted The planets in alphabetical order sorted(planets)

primes = [2, 3, 5, 7]
print(sum(primes))
print(min(primes))
print(max(primes))

# list.append modifies a list by adding an item to the end:
planets.append("Pluto")
print(planets)

# list.pop removes and returns the last element of a list:
planets.pop()
print(planets)


# Where does Earth fall in the order of planets?
planet_index = planets.index('Earth') # Search list
print(planet_index)

print('Earth' in planets)
print('Calbefraques' in planets)

new_planets = planets + ['Pluto']
print(new_planets)

copy_planets = ['Mercur', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets == copy_planets)  # True
print(planets == ['Mercury'])   # False

print(planets[2])    # Earth
print(planets[-1])   # Neptune

print(planets > ['A'])  # True (because 'Mercur' > 'A')

planets.extend(['Pluto', 'Eris']) # Add multiple elements to the end
print(planets)

