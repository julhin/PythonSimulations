import random
import numpy as np
from array import *
import container


wound_chart = [
        ["4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-", "-"],
        ["4", "4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-"],
        ["3", "4", "4", "5", "5", "6", "6", "6/4", "6/5","6/6"],
        ["3", "3", "4", "4", "5", "5", "6", "6", "6/4","6/5"],
        ["3", "3", "3", "4", "4", "5", "5", "6", "6","6/4"],
        ["3", "3", "3", "3", "4", "4", "5", "5", "6","6"],
        ["3", "3", "3", "3", "3", "4", "4", "5", "5","6"],
        ["3", "3", "3", "3", "3", "3", "4", "4", "5","5"],
        ["3", "3", "3", "3", "3", "3", "3", "4", "4","5"],
        ["3", "3", "3", "3", "3", "3", "3", "3", "4","4"],
        ]
# wound chart as dict, dict currently removes duplicates
# wound_chart = {
#     "1": {"4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-", "-"],
#     "2": {"4", "4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-"],
#     "3": {"3", "4", "4", "5", "5", "6", "6", "6/4", "6/5","6/6"],
#     "4": {"3", "3", "4", "4", "5", "5", "6", "6", "6/4","6/5"],
#     "5": {"3", "3", "3", "4", "4", "5", "5", "6", "6","6/4"],
#     "6": {"3", "3", "3", "3", "4", "4", "5", "5", "6","6"],
#     "7": {"3", "3", "3", "3", "3", "4", "4", "5", "5","6"],
#     "8": {"3", "3", "3", "3", "3", "3", "4", "4", "5","5"],
#     "9": {"3", "3", "3", "3", "3", "3", "3", "4", "4","5"],
#     "10": {"3", "3", "3", "3", "3", "3", "3", "3", "4","4"],
# ]

def dice_roll(sides = 6):
    return random.randint(1,sides)

def ranged_attack(atk_strength, def_defense):
    value = compare_characteristics(atk_strength, def_defense)

    if (value == -1):
        return False
    if (value.__contains__('/')):
        tmp = value.split('/')
        if (len(tmp) != 2):
            #raise error -> data is corrupt
            return false 
        roll = dice_roll()
        if (roll >= value[0]):
            return dice_roll() >= value[1]
    return dice_roll() >= int(value)

def compare_characteristics(strength, defense):
    value = wound_chart[strength][defense]
    if (value == '-'):
        return -1
    return value


def main():

    for i in range (0,10):
        print(wound_chart[i])
    seen = [0] * 6
    print(seen)
    for i in range(100):

        x = dice_roll()
        # value back to array index in stupid bc I am no python wizard
        tmp = seen[x-1]
        seen[x-1] = tmp + 1
    print(seen)

    dale_archer = container.Unit(6, '4/3', 4, 5, 1, 1, 4)
    print(dale_archer.toString())

    for i in range(10):

        if (ranged_attack(3, 6) == True):
            print("Hit")
        else:
            print("Miss")


if __name__ == "__main__":
    main()    