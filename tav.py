import random

class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0

        self.assign_stats()

    def assign_stats(self) -> None:
        standard = [15, 14, 13, 12, 10, 8]
        random.shuffle(standard)

        self.strength = standard[0]
        self.dexterity = standard[1]
        self.constitution = standard[2]
        self.charisma = standard[3]
        self.intelligence = standard[4]
        self.wisdom = standard[5]

    def print_character_sheet(self) -> None:
        fire = '\U0001F525'
        sword = '\U00002694'
        
        print('====== ' + fire + ' BLUDGEONS & FLAGONS ' + fire + ' ======')
        print('Name: ' + self.name)
        print('Role: ' + self.role)
        print('--------- ' + sword + ' CHARACTER STATS ' + sword + ' ---------')
        print('Strength         ' + str(self.strength))
        print('Dexterity        ' + str(self.dexterity))
        print('Constitution     ' + str(self.constitution))
        print('Charisma         ' + str(self.charisma))
        print('Intelligence     ' + str(self.intelligence))
        print('Wisdom           ' + str(self.wisdom))
        print('---------------------------------------')

    def roll(self, input: str) -> int:
        return 20
