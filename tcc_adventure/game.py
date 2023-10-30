from .characters.character_manager import create_character


def main():
    character = create_character()
    print(character)


if __name__ == "__main__":
    main()
