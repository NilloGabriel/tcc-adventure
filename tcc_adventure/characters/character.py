class Character:
    def __init__(self, name, character_class, race, equipment, abilities):
        self.name = name
        self.character_class = character_class
        self.race = race
        self.equipment = equipment
        self.abilities = abilities

    def __str__(self):
        return (
            f"===== Ficha de Personagem de RPG =====\n"
            f"Nome: {self.name}\n"
            f"Classe: {self.character_class['name']}\n"
            f"Raça: {self.race['name']}\n\n"
            f"Equipamentos: \n{self.list_equipment()}\n\n"
            f"Habilidades: \n{self.list_abilities()}\n"
            f"===== Fim da Ficha de Personagem ====="
        )

    def list_equipment(self):
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(self.equipment)])

    def list_abilities(self):
        return "\n".join([f"{i+1}. {ability}" for i, ability in enumerate(self.abilities)])
