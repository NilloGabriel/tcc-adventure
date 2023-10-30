import json
import os
from .character import Character


def create_character():
    print("===== Cadastro Ficha de Personagem de RPG =====")

    name = input_name()

    classes, races, abilities, equipment = load_data()

    character_class = select_option(classes, "Classe")
    race = select_option(races, "Raça")

    equipment = select_equipment(character_class, race, equipment)
    abilities = select_abilities(character_class, race, abilities)

    return Character(name, character_class, race, equipment, abilities)


def input_name():
    while True:
        name = input("Nome: ").strip()
        if name.isalpha():
            return name
        else:
            print("O nome deve conter apenas letras. Tente novamente.")


def load_data():
    base_path = os.path.dirname(__file__)
    classes_path = os.path.join(base_path, "..", "data", "classes.json")
    races_path = os.path.join(base_path, "..", "data", "races.json")
    abilities_path = os.path.join(base_path, "..", "data", "abilities.json")
    equipment_path = os.path.join(base_path, "..", "data", "equipment.json")

    with open(classes_path, "r") as file:
        classes = json.load(file)["classes"]

    with open(races_path, "r") as file:
        races = json.load(file)["races"]

    with open(abilities_path, "r") as file:
        abilities = json.load(file)["abilities"]

    with open(equipment_path, "r") as file:
        equipment = json.load(file)["equipment"]

    return classes, races, abilities, equipment


def select_option(data, category):
    print(f"\nEscolha uma opção para {category}: ")
    for i, option in enumerate(data, start=1):
        print(f"{i}. {option['name']}")

    while True:
        choice = input("Opção: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(data):
                return data[choice - 1]
        print("Opção inválida. Tente novamente.")


def select_equipment(character_class, race, equipment_data):
    equipment = equipment_data.get(
        character_class["name"], {}).get(race["name"], {}).get("weapons", [])

    print("\nEquipamentos disponíveis:")
    for i, item in enumerate(equipment, start=1):
        print(f"{i}. {item}")

    while True:
        choice = input("Opção: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(equipment):
                return [equipment[choice - 1]]
        print("Opção inválida. Tente novamente.")


def select_abilities(character_class, race, abilities_data):
    abilities = abilities_data.get(
        character_class["name"], {}).get(race["name"], [])

    print("\nHabilidades disponíveis:")
    for i, ability in enumerate(abilities, start=1):
        print(f"{i}. {ability}")

    while True:
        choice = input("Opção: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(abilities):
                os.system('cls' if os.name == 'nt' else 'clear')
                return [abilities[choice - 1]]
        print("Opção inválida. Tente novamente.")
