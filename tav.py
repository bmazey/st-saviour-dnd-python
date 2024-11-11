import random
from draw import draw_d4, draw_d20

class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.level = 1

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
        print('Name:  ' + self.name)
        print('Role:  ' + self.role)
        print('Level: ' + self.level)
        print('--------- ' + sword + ' CHARACTER STATS ' + sword + ' ---------')
        print('Strength         ' + str(self.strength))
        print('Dexterity        ' + str(self.dexterity))
        print('Constitution     ' + str(self.constitution))
        print('Charisma         ' + str(self.charisma))
        print('Intelligence     ' + str(self.intelligence))
        print('Wisdom           ' + str(self.wisdom))
        print('---------------------------------------')

    def roll(self, buff: str) -> int:
        if buff == 'a':
            first = random.randint(1, 20)
            draw_d20(first)

            second = random.randint(1, 20)
            draw_d20(second)

            if first > second:
                return first
            else:
                return second
        elif buff == 'g':
            roll = random.randint(1, 20)
            draw_d20(roll)

            guidance = random.randint(1, 4)
            draw_d4(guidance)

            return roll + guidance
        else:
            roll = random.randint(1, 20)
            draw_d20(roll)

            return roll
