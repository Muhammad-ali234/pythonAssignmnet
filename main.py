class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def feed(self):
        print(f"{self.name} the {self.species} is being fed.")
    
    def make_sound(self):
        pass


class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} the {self.species} is giving birth to live young.")
    
    def nurse(self):
        print(f"{self.name} the {self.species} is nursing.")


class Bird(Animal):
    def lay_eggs(self):
        print(f"{self.name} the {self.species} is laying eggs.")
    
    def fly(self):
        print(f"{self.name} the {self.species} is flying.")


class Lion(Mammal):
    def make_sound(self):
        print(f"{self.name} the Lion roars: Roarrrr!")


class Parrot(Bird):
    def make_sound(self):
        print(f"{self.name} the Parrot mimics: Squawk!")


class Elephant(Mammal):
    def use_trunk(self):
        print(f"{self.name} the Elephant is using its trunk.")
    
    def social_interaction(self):
        print(f"{self.name} the Elephant is interacting socially within the herd.")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} the Penguin is swimming.")
    
    def nesting(self):
        print(f"{self.name} the Penguin is nesting.")


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()
    
    def make_all_animals_sounds(self):
        for animal in self.animals:
            animal.make_sound()


def main():
    zoo = Zoo()
    create_initial_zoo(zoo)
    manage_zoo(zoo)


def create_initial_zoo(zoo):
    lion = Lion("Simba", "Lion", 5)
    parrot = Parrot("Polly", "Parrot", 2)
    elephant = Elephant("Dumbo", "Elephant", 10)
    penguin = Penguin("Pingu", "Penguin", 3)
    
    zoo.add_animal(lion)
    zoo.add_animal(parrot)
    zoo.add_animal(elephant)
    zoo.add_animal(penguin)


def manage_zoo(zoo):
    while True:
        print("\nWelcome to the Zoo Management System!")
        print("1. Feed all animals")
        print("2. Make all animals make sounds")
        print("3. Add a new animal to the zoo")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            zoo.feed_all_animals()
        elif choice == "2":
            zoo.make_all_animals_sounds()
        elif choice == "3":
            add_animal_to_zoo(zoo)
        elif choice == "4":
            print("Exiting the Zoo Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_animal_to_zoo(zoo):
    print("\nAdd an animal to the zoo:")
    name = input("Enter the name of the animal: ")
    species = input("Enter the species of the animal: ")
    age = int(input("Enter the age of the animal: "))
    
    # Let the user choose the type of animal to add
    print("Select the type of animal:")
    print("1. Lion")
    print("2. Parrot")
    print("3. Elephant")
    print("4. Penguin")
    animal_choice = input("Enter your choice: ")
    
    if animal_choice == "1":
        animal = Lion(name, species, age)
    elif animal_choice == "2":
        animal = Parrot(name, species, age)
    elif animal_choice == "3":
        animal = Elephant(name, species, age)
    elif animal_choice == "4":
        animal = Penguin(name, species, age)
    else:
        print("Invalid choice.")
        return
    
    zoo.add_animal(animal)
    print(f"{name} the {species} has been added to the zoo.")


if __name__ == "__main__":
    main()
