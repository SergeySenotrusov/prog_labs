while True:
    try:
        min_population = int(input("Enter the number: "))
        break
    except ValueError:
        print("Incorrect input. Please enter a number")


cities = []

with open('cities.txt', 'r') as file:
    for line in file:
        city, population = line.strip().split(':')
        if int(population) > min_population:
            cities.append((city, int(population)))

cities.sort(key=lambda x: x[0])

with open('filtered_cities.txt', 'w') as file:
    for city, population in cities:
        file.write(f"{city}:{population}\n")