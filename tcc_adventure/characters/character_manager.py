from .character import Character
from ..utils.data_loader import load_classes, load_races, load_abilities, load_equipment
from ..utils.input_validation import get_valid_alpha_input, get_valid_numeric_input
from ..utils.generics import select_option_generic


def create_character():
    print("===== Cadastro Ficha de Personagem de RPG =====")

    name = get_valid_alpha_input("Nome: ")
    character_class = select_option_generic(load_classes(), "Classe")
    race = select_option_generic(load_races(), "Raça")
    equipment = select_equipment(character_class, race)
    abilities = select_abilities(character_class, race)

    return Character(name, character_class, race, equipment, abilities)


def select_equipment(character_class, race):
    equipment_data = load_equipment()
    equipment = equipment_data.get(character_class['name'], {}).get(
        race['name'], {}).get("weapons", [])

    print("\nEquipamentos disponíveis:")
    for i, item in enumerate(equipment, start=1):
        print(f"{i}. {item}")

    selected_equipment = [
        equipment[get_valid_numeric_input("Opção: ", equipment) - 1]]
    return selected_equipment


def select_abilities(character_class, race):
    abilities_data = load_abilities()
    abilities = abilities_data.get(
        character_class['name'], {}).get(race['name'], [])

    print("\nHabilidades disponíveis:")
    for i, ability in enumerate(abilities, start=1):
        print(f"{i}. {ability}")

    selected_abilities = [
        abilities[get_valid_numeric_input("Opção: ", abilities) - 1]]
    return selected_abilities
