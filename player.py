import random
from draw import draw_d20, draw_d4

class Player:
    def __init__(self, name: str, role: str, strength: int):
        self.name = name
        self.role = role
        self.strength = strength
        self.hp = 100

    def roll_d20(self) -> int:
        roll = random.randint(1, 20)
        draw_d20(roll)
        return roll

    def roll_advantage(self) -> int:
        first_roll = random.randint(1, 20)
        draw_d20(first_roll)

        second_roll = random.randint(1, 20)
        draw_d20(second_roll)

        if first_roll > second_roll:
            return first_roll
        else:
            return second_roll

    def attack(self) -> None:
        print(self.name + " the " + self.role + " attacks!")

