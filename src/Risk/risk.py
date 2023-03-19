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
    for i in range(0, len(defender)):
        if (defender[i] >= attacker[i]):
            casAtk = casAtk + 1
        else:
            casDef = casDef + 1
    return (casAtk, casDef)


def fight(attacker: int, defender: int):
    # fight sequence
    while True:
        print(f"Armies attacker: {attacker}")
        print(f"Armies defender: {defender}")
        # how to
        if (attacker == 0):
            return defender
        if (defender == 0):
            return attacker

        atkDice = checkDiceAtttacker(attacker)
        defDice = checkDiceDefender(defender)

        result = battleRound(atkDice, defDice)
        print(f"attacker: {result[0]}")
        print(f"defender: {result[1]}")
        attacker = attacker - result[0]
        defender = defender - result[1]

    # check if one side is killed

    # check how may atacker dice

    # check defender dice

    # roll dice

    # remove casualties

    # goto new round


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
    fight(10, 5)
