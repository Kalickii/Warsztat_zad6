import re
from random import randint

def dice(code):
    """
    Dice roll.
    User input, how many throws, which type of dice, and additional modifier he want to use in the simulation.
    :param code: xDy+z  where: x = throws, Dy = type of dice, z = additional modifier ex. '2D10+10'
    :rtype: int
    :return: Function returns simulation of the dice roll.
    """
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    throws = 0
    valid_dice = 0
    modifier = 0

    try:
        found_dice = re.findall(r"D\d+", code)[0]
        if found_dice in dice_types:
            valid_dice = int(found_dice[1::])

        if "D" == code[0]:
            throws = 1
        else:
            throws = int(re.findall(r"\d+", code)[0])

        modifier = int(re.findall(r"\d+", code)[-1])
        if "-" in code:
            modifier *= -1
        if "-" not in code and "+" not in code:
            modifier = 0
    except IndexError:
        print("Invalid code")
    except TypeError:
        print("Invalid code")
    result = throws * randint(1, valid_dice) + modifier
    return result

player_points = 0
computer_points = 0

play = input("Press Enter to throw the dices: ")
while play != "":
    play = input("Press Enter! ")

throw = randint(1, 6) + randint(1, 6)
player_points += throw

comp_throw = randint(1, 6) + randint(1, 6)
computer_points += comp_throw

print(f"Your score is: {player_points}")
print(f"Computer score is: {computer_points}")

play = input("Press Enter to throw the dices: ")
while player_points < 2001 and computer_points < 2001:
    throw = 0
    comp_throw = 0
    while play != "":
        play = input("Press Enter! ")

    throw = randint(1, 6) + randint(1, 6)
    if throw == 7:
        player_points //= throw
    elif throw == 11:
        player_points *= throw
    else:
        player_points += throw

    comp_throw = randint(1, 6) + randint(1, 6)
    if comp_throw == 7:
        computer_points //= comp_throw
    elif comp_throw == 11:
        computer_points *= comp_throw
    else:
        computer_points += comp_throw

    print(f"Your score is: {player_points}")
    print(f"Computer score is: {computer_points}")

    if player_points >= 2001:
        print("You win!")
        break
    elif computer_points >= 2001:
        print("You lose!")
        break
    play2 = input("Press Enter to throw the dices: ")

