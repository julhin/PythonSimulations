import random

max_atk_dice = 3
max_def_dice = 3


def dice_roll(sides=6):
    return random.randint(1, sides)


def checkDiceAtttacker(armies: int):
    if armies >= max_atk_dice:
        return max_atk_dice
    return armies


def checkDiceDefender(armies: int):
    if armies >= max_def_dice:
        return max_def_dice
    return armies


def battleDiceRoll(dice: int):
    tmp = []
    for i in range(0, dice):
        tmp.append(dice_roll())
    return tmp


def battleRound(atkDice: int, defDice: int):
    attacker = battleDiceRoll(atkDice)
    defender = battleDiceRoll(defDice)
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    # compare resulst and return casualaties
    print(attacker)
    print(defender)
    casAtk = 0
    casDef = 0

    if (len(defender) <= len(attacker)):
        dicetocheck = len(defender)
    else:
        dicetocheck = len(attacker)

    for i in range(0, dicetocheck):
        if (defender[i] >= attacker[i]):
            casAtk = casAtk + 1
        else:
            casDef = casDef + 1
    return (casAtk, casDef)


def battle(attacker: int, defender: int):
    # fight sequence
    while True:
        # print(f"Armies attacker: {attacker}")
        # print(f"Armies defender: {defender}")
        # how to
        if (attacker == 0):
            return 0
        if (defender == 0):
            return 1

        atkDice = checkDiceAtttacker(attacker)
        defDice = checkDiceDefender(defender)

        result = battleRound(atkDice, defDice)
        # print(f"attacker: {result[0]}")
        # print(f"defender: {result[1]}")
        attacker = attacker - result[0]
        defender = defender - result[1]


if __name__ == "__main__":
    while True:
        s = input("Def dice (2,3)? ")
        try:
            x = int(s)
            break
        except:
            print("please enter valid input")
            continue

    max_def_dice = x
    battleResults = []
    for i in range(100):
        battleResults.append(battle(10, 5))
    print(battleResults)
