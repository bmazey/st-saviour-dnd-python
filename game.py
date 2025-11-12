import random
import time

from player import Player
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

    # name = input('Name: ')
    # print('Welcome ' + name + ' ...')

    player_1 = Player('Angel Fre', 'Doctor', 10)
    option = input('Press A to roll advantage or Enter to roll a d20 ')
    option.lstrip()
    if option.lower() == 'a':
        player_1.roll_advantage()
    else:
        player_1.roll_d20()
    # roll = player_1.roll_d20()
    # print_dramatic_text(player_1.name + ' rolled a ' + str(roll) + ' ...')
    # player_1.attack()
    # roll = player_1.roll_advantage()
    # print_dramatic_text(player_1.name + ' rolled a ' + str(roll) + ' with advantage!')

    # player_2 = Player('Miranda', 'Barbarian', 20)
    # player_2.attack()

    # name = input('Name: ')
    # role = input('Role: ')

    # player = Player(name, role, 10)
    # print('Your name is ' + player.name + ' and your role is ' + player.role + '.')
    # print_dramatic_text('Our adventure begins in a shady tavern ...')

    # input('Press Enter to roll a d6.')
    # roll = random.randint(1, 6)
    # draw_d6(roll)
