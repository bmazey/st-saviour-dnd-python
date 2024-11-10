import random
import time

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

    wins = 0
    while True:
        print()
        print_dramatic_text('A monster approaches!')

        requirement = generate_monster()
        buff = input('Press \'a\' for advantage, \'g\' for guidance, & Enter to roll:')

        result = tav.roll(buff)

        if result < requirement:
            print()
            print_dramatic_text('You needed ' + requirement + ', you rolled ' + result + ' ...')
            print()
            print_dramatic_text('       G A M E   O V E R')
            print()
            break
        if result == 1:
            print()
            print_dramatic_text('       CRITICAL FAILURE')
            print()
            print_dramatic_text('       G A M E   O V E R')
            print()
            break
        if result == 20:
            wins += 1
            print()
            print_dramatic_text('       CRITICAL SUCCESS')
            print()
        else:
            wins += 1
            print()
            print_dramatic_text('You needed ' + requirement + ', you rolled ' + result + ' ... well done!')
            print()

        if wins >= 3:
            print()
            print_dramatic_text(tav.name + ' the ' + tav.role + ' has completed the long journey!')
            print()
            print_dramatic_text('           {  fin  }')
            break
