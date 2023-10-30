import json
import os
from .character import Character
from ..utils.data_loader import load_classes, load_races, load_abilities, load_equipment


def create_character():
    print("===== Cadastro Ficha de Personagem de RPG =====")

    name = input_name()

    character_class = select_option(load_classes(), "Classe")
    race = select_option(load_races(), "Raça")
    equipment = select_equipment(character_class, race)
    abilities = select_abilities(character_class, race)

    return Character(name, character_class, race, equipment, abilities)


def input_name():
    while True:
        name = input("Nome: ").strip()
        if name.isalpha():
            return name
        else:
            print("O nome deve conter apenas letras. Tente novamente.")


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


def select_equipment(character_class, race):
    equipment_data = load_equipment()
    equipment = equipment_data.get(character_class['name'], {}).get(
        race['name'], {}).get("weapons", [])

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


def select_abilities(character_class, race):
    abilities_data = load_abilities()
    abilities = abilities_data.get(
        character_class['name'], {}).get(race['name'], [])

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
