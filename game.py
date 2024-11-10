import random
import time

from draw import draw_d4, draw_d20
from tav import Tav

def generate_monster() -> int:
    r = random.randint(1, 6)
    if r == 1 or r == 2 or r == 3:
        print('zombie')
        return 8
    if r == 4 or r == 5:
        print('mimic')
        return 12
    if r == 6:
        print('beholder')
        return 18

    return -1

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # calculate player initiatve to see who goes first 
    # any critical success / failure?
    # draw result

    name = input('Name: ')
    role = input('Role: ')

    tav = Tav(name, role)
    tav.print_character_sheet()

    print_dramatic_text('Our adventure begins in a shady tavern ...')

    # d20(20)
