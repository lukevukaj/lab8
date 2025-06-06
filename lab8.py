# SDM:
# This program is a simple Pet Store program.
# It lets the user add (register) new pets, view pets, adopt pets, rename pets, and remove (deregister) pets.
# Each pet is a Pet object with a name, species, age, and adopted status.
# All pets are stored in a dictionary with a unique ID for easy access.
# The user can interact with the program through a simple text menu.

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = False


    def __str__(self):
        status = "Adopted" if self.adopted else "Available"
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Status: {status}"

def register_pet(pets, next_id):
    name = input("What's the pet's name? ")
    species = input("What type of animal is it? ")
    age = input("How old is it? ")
    pet = Pet(name, species, age)
    pets[next_id] = pet
    print(f"Nice! Added {name} to the store with ID {next_id}.")
    return next_id + 1

def view_pets(pets):
    if not pets:
        print("No pets here yet. Gotta add some!")
    else:
        print("Here are the pets currently in the store:")
        for pet_id, pet in pets.items():
            print(f"[ID {pet_id}] {pet}")


def adopt_pet(pets):
    pet_id = int(input("Enter the ID of the pet you want to adopt: "))
    if pet_id in pets:
        pets[pet_id].adopted = True
        print(f"Congrats! {pets[pet_id].name} has been adopted.")
    else:
        print("Hmm... that pet ID doesn't exist.")

def rename_pet(pets):
    pet_id = int(input("Enter the ID of the pet you want to rename: "))
    if pet_id in pets:
        new_name = input("What's the new name? ")
        old_name = pets[pet_id].name
        pets[pet_id].name = new_name
        print(f"{old_name} is now named {new_name}.")
    else:
        print("Can't find that pet ID.")


def remove_pet(pets):
    pet_id = int(input("Enter the ID of the pet to remove: "))
    if pet_id in pets:
        removed_pet = pets.pop(pet_id)
        print(f"Removed {removed_pet.name} from the store.")
    else:
        print("Invalid ID — no pet removed.")

def run_pet_store():
    pets = {}
    next_id = 1
    running = True
    print("🐾 Welcome to the Pet Store! 🐾")
    while running:
        print("\nWhat would you like to do?")
        print("1. Add a new pet")
        print("2. See all pets")
        print("3. Mark a pet as adopted")
        print("4. Rename a pet")
        print("5. Remove a pet")
        print("6. Exit the program")
        choice = input("Type your choice (1-6): ")
        if choice == "1":
            next_id = register_pet(pets, next_id)
        elif choice == "2":
            view_pets(pets)
        elif choice == "3":
            adopt_pet(pets)
        elif choice == "4":
            rename_pet(pets)
        elif choice == "5":
            remove_pet(pets)
        elif choice == "6":
            print("See ya! Thanks for visiting the Pet Store.")
            running = False
        else:
            print("Oops, that's not a valid option. Try again!")

run_pet_store()
