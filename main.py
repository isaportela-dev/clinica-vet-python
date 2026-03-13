class Pet:
    def __init__(self, name, species, age, owner):
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner


pets = []


def show_menu():
    print("\n=== Veterinary Clinic System ===")
    print("1 - Register pet")
    print("2 - List pets")
    print("3 - Search pet")
    print("4 - Remove pet")
    print("5 - Exit")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_valid_age():
    while True:
        age = input("Pet age: ").strip()
        if age.isdigit() and int(age) >= 0:
            return int(age)
        print("Invalid age. Please enter a valid number.")


def register_pet():
    print("\n--- Register Pet ---")
    name = get_non_empty_input("Pet name: ")
    species = get_non_empty_input("Species: ")
    age = get_valid_age()
    owner = get_non_empty_input("Owner name: ")

    pet = Pet(name, species, age, owner)
    pets.append(pet)

    print(f"\n{name} was registered successfully.")


def list_pets():
    print("\n--- Registered Pets ---")

    if not pets:
        print("No pets registered yet.")
        return

    for index, pet in enumerate(pets, start=1):
        print(f"\nPet #{index}")
        print(f"Name: {pet.name}")
        print(f"Species: {pet.species}")
        print(f"Age: {pet.age}")
        print(f"Owner: {pet.owner}")
        print("-" * 25)


def search_pet():
    print("\n--- Search Pet ---")
    search_name = get_non_empty_input("Enter the pet name: ")

    for pet in pets:
        if pet.name.lower() == search_name.lower():
            print("\nPet found:")
            print(f"Name: {pet.name}")
            print(f"Species: {pet.species}")
            print(f"Age: {pet.age}")
            print(f"Owner: {pet.owner}")
            return

    print("Pet not found.")


def remove_pet():
    print("\n--- Remove Pet ---")
    name_to_remove = get_non_empty_input("Enter the pet name to remove: ")

    for pet in pets:
        if pet.name.lower() == name_to_remove.lower():
            pets.remove(pet)
            print(f"{pet.name} was removed successfully.")
            return

    print("Pet not found.")


def main():
    print("Veterinary Clinic System started!")

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            register_pet()
        elif option == "2":
            list_pets()
        elif option == "3":
            search_pet()
        elif option == "4":
            remove_pet()
        elif option == "5":
            print("Closing system...")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()