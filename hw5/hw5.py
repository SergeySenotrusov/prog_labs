import random
import datetime
import pprint
import time

def log(message=None):
    try:
        with open('logs.log', 'a') as f:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if message:
                f.write(f"{current_time} -- {message}\n\n")
            else:
                f.write(f"{current_time} -- program start\n\n\n")
    except Exception as e:
        pass

class Animal:
    def __init__(self, species, size, food, eco_niche, lifespan, gender, fullness):
        self.id = id(self)
        self.species = species
        self.size = size
        self.food = food
        self.eco_niche = eco_niche
        self.lifespan = lifespan
        self.gender = gender
        self.age = 0
        self.fullness = fullness

    def __del__(self):
        try:
            log(f'animal {self.species} (ID: {self.id}) dead')
        except Exception as e:
            print(f"Error in __del__ method: {e}")

class Planet:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000

        self.dict_species = {
            'water': {
                'species': ['orca', 'shark', 'cancer', 'squid'],
                'size': [10000, 5000, 5, 5],
                'food': [['shark', 'cancer', 'squid'], ['cancer', 'squid'], 'plant', 'plant'],
                'lifespan': [20, 40, 15, 10],
                'fullness': [40, 40, 40, 40]
            },
            'land': {
                'species': ['bear', 'lion', 'giraffe', 'elephant'],
                'size': [2000, 500, 1000, 10000],
                'food': [['lion', 'giraffe', 'elephant'], ['lion', 'giraffe', 'elephant'], 'plant', 'plant'],
                'lifespan': [20, 20, 15, 15],
                'fullness': [50, 50, 50, 50]
            },
            'air': {
                'species': ['falcon', 'eagle', 'parrot', 'dove'],
                'size': [20, 10, 5, 5],
                'food': [['parrot', 'dove'], ['parrot', 'dove'], 'plant', 'plant'],
                'lifespan': [10, 10, 10, 10],
                'fullness': [60, 60, 60, 60]
            }
        }

    def add_plant_food(self, amount):
        self.plant_food += amount
        log(f'added {amount} units of food')

    def add_animal(self):
        spic = input('enter the species you want to create: ').lower()

        gender = ''
        while gender not in ['male', 'female']:
            gender = input('enter the gender (male/female): ').lower()
            if gender not in ['male', 'female']:
                print("invalid input. Please enter 'male' or 'female'.")

        found = False
        for environment in self.dict_species:
            if spic in self.dict_species[environment]['species']:
                index = self.dict_species[environment]['species'].index(spic)
                size = self.dict_species[environment]['size'][index]
                food = self.dict_species[environment]['food'][index]
                eco_niche = environment
                lifespan = self.dict_species[environment]['lifespan'][index]
                fullness = self.dict_species[environment]['fullness'][index]

                new_animal = Animal(spic, size, food, eco_niche, lifespan, gender, fullness)
                self.animals.append(new_animal)
                found = True
                print(f"Added new animal: {spic}")
                break

        if not found:
            print(f"Species '{spic}' not found in the ecosystem dictionary.")

        log('animal add')

    def display_animal_info(self, idd=None):
        if idd:
            animal = next((animal for animal in self.animals if animal.id == idd), None)
            if animal:
                log(f"id: {animal.id}, species: {animal.species}, size: {animal.size}, food: {animal.food}, "
                      f"eco_niche: {animal.eco_niche}, lifespan: {animal.lifespan}, age: {animal.age}, "
                      f"fullness: {animal.fullness}, gender: {animal.gender}")
        else:
            for animal in self.animals:
                log(f"id: {animal.id}, species: {animal.species}, size: {animal.size}, food: {animal.food}, "
                      f"eco_niche: {animal.eco_niche}, lifespan: {animal.lifespan}, age: {animal.age}, "
                      f"fullness: {animal.fullness}, gender: {animal.gender}")
        print('\n')

    def display_species_info(self):
        log('the following species are available for creation:\n')
        log (pprint.pprint(self.dict_species))

    def reproduction(self, parent1_id, parent2_id):
        parent1 = next((animal for animal in self.animals if animal.id == parent1_id), None)
        parent2 = next((animal for animal in self.animals if animal.id == parent2_id), None)

        if not parent1 or not parent2:
            print("One or both parents not found.")
            return

        if parent1.species != parent2.species:
            print("Both parents must be of the same species.")
            return

        if parent1.gender == parent2.gender:
            print("Parents must be of different genders.")
            return

        if parent1.fullness <= 50 and parent1.eco_niche == "water":
            print("Water animals need more than 50% fullness to reproduction.")
            return

        if parent2.fullness <= 50 and parent2.eco_niche == "water":
            print("Water animals need more than 50% fullness to reproduction.")
            return

        if parent1.fullness <= 42 and parent1.age <= 3 and parent1.eco_niche == "air":
            print("Air animals need more than 42% fullness and age more than 3 to reproduction.")
            return

        if parent2.fullness <= 42 and parent2.age <= 3 and parent2.eco_niche == "air":
            print("Air animals need more than 42% fullness and age more than 3 to reproduction.")
            return

        if parent1.fullness <= 20 and parent1.age <= 5 and parent1.eco_niche == "land":
            print("Land animals need more than 20% fullness and age more than 5 to reproduction.")
            return

        if parent2.fullness <= 20 and parent2.age <= 5 and parent2.eco_niche == "land":
            print("Land animals need more than 20% fullness and age more than 5 to reproduction.")
            return

        num_offspring = 0
        offspring_fullness = 0
        if parent1.eco_niche == "water":
            num_offspring = 10
            offspring_fullness = 23
        elif parent1.eco_niche == "air":
            num_offspring = 4
            offspring_fullness = 64
        elif parent1.eco_niche == "land":
            num_offspring = 2
            offspring_fullness = 73

        for _ in range(num_offspring):
            gender = random.choice(["male", "female"])
            new_animal = Animal(parent1.species, parent1.size, parent1.food, parent1.eco_niche, parent1.lifespan, gender, offspring_fullness)
            self.animals.append(new_animal)

        log('reproduction event')

    def advance_time(self):
        while self.animals:
            new_animals = []
            for animal in self.animals:
                animal.age += 1
                if animal.age >= animal.lifespan:
                    self.plant_food += animal.size
                    log(f"animal {animal.species} (ID: {animal.id}) died of old age and converted to {animal.size} units of plant food")
                else:
                    new_animals.append(animal)
            self.animals = new_animals

            for animal in self.animals:
                if 'plant' in animal.food:
                    if self.plant_food > 0:
                        animal.fullness += 26
                        self.plant_food -= 1
                        log(f"animal {animal.species} (ID: {animal.id}) ate plant food and increased fullness to {animal.fullness}")
                    else:
                        animal.fullness -= 9
                        log(f"animal {animal.species} (ID: {animal.id}) couldn't find plant food and decreased fullness to {animal.fullness}")
                else:
                    success = random.random() < 0.5
                    if success:
                        prey_species = random.choice(animal.food)
                        prey = next((prey for prey in self.animals if prey.species == prey_species), None)
                        if prey:
                            self.animals.remove(prey)
                            animal.fullness += 53
                            log(f"animal {animal.species} (ID: {animal.id}) successfully hunted {prey_species} (ID: {prey.id}) and increased fullness to {animal.fullness}")
                        else:
                            animal.fullness -= 16
                            log(f"animal {animal.species} (ID: {animal.id}) couldn't find prey and decreased fullness to {animal.fullness}")
                    else:
                        animal.fullness -= 16
                        log(f"animal {animal.species} (ID: {animal.id}) couldn't catch prey and decreased fullness to {animal.fullness}")

            new_animals = []
            for animal in self.animals:
                if animal.fullness < 10:
                    self.plant_food += animal.size
                    log(f"animal {animal.species} (ID: {animal.id}) died of starvation and converted to {animal.size} units of plant food")
                else:
                    new_animals.append(animal)
            self.animals = new_animals

            log('time advanced by 1 unit\n')
            time.sleep(2)
            self.display_animal_info()

# перед запуском программы создать logs.log, запустить tail -f logs.log
log()
Planet = Planet()

flag = ''
while flag != 'stop':
    Planet.add_animal()
    flag = input('stop? ')

Planet.advance_time()




