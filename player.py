class Player:
    def __init__(self, name: str, role: str, strength: int):
        self.name = name
        self.role = role
        self.strength = strength
        self.hp = 100

    def attack(self) -> None:
        print(self.name + " the " + self.role + " attacks!")

