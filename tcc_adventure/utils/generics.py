from .input_validation import get_valid_numeric_input


def select_option_generic(data, category):
    print(f"\nEscolha uma opção para {category}: ")
    for i, option in enumerate(data, start=1):
        print(f"{i}. {option['name']}")

    return data[get_valid_numeric_input("Opção: ", data) - 1]
