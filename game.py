import random
import time

from draw import draw_d20, draw_d6, draw_d4

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
    # any critical success / failure?

    name = input('Name: ')
    role = input('Role: ')

    print('Your name is ' + name + ' and your role is ' + role + '.')
    print_dramatic_text('Our adventure begins in a shady tavern ...')

    input('Press Enter to roll a d20.')
    roll = random.randint(1, 20)
    draw_d20(roll)
