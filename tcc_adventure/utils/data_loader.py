import json
import os


def load_data(data_type):
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "..", "database",
                             "db_input", f"{data_type}.json")

    with open(data_path, "r") as file:
        data = json.load(file)
        return data.get(data_type, {})


def load_classes():
    return load_data("classes")


def load_races():
    return load_data("races")


def load_abilities():
    return load_data("abilities")


def load_equipment():
    return load_data("equipment")
