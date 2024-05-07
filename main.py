import re
from random import randint, choice

def dice():
    """
    Dice roll.
    User input which type of dice he want to throw.
    :rtype: int
    :return: Function returns the result of two throws of the chosen dice.
    """
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    throws = 2
    valid_dice = 0
    result = 0
    code = ""

    while code not in dice_types:
        try:
            code = input("Enter a dice type: ")
            if code in dice_types:
                valid_dice = int(code[1::])
            else:
                print("Invalid dice type")
        except ValueError:
            print("Invalid code")
        except IndexError:
            print("Invalid code")
        except TypeError:
            print("Invalid code")

    for x in range(throws):
        result += randint(1, valid_dice)
    return result

def comp_dice():
    """
    Computer dice roll.
    Function randomly picks computer dice type and simulates the throws.
    :rtype: int
    :return: Function returns the result of two throws of the chosen dice.
    """
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    throws = 2
    valid_dice = 0
    result = 0

    code = choice(dice_types)
    valid_dice = int(code[1::])

    for x in range(throws):
        result += randint(1, valid_dice)
    return result

player_points = 0
computer_points = 0

dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
print(dice_types)

throw = randint(1, dice()) + randint(1, dice())
player_points += throw

comp_throw = randint(1, comp_dice()) + randint(1, comp_dice())
computer_points += comp_throw

print(f"Your score is: {player_points}")
print(f"Computer score is: {computer_points}")

while player_points < 2001 and computer_points < 2001:
    throw = randint(1, dice()) + randint(1, dice())
    if throw == 7:
        player_points //= throw
    elif throw == 11:
        player_points *= throw
    else:
        player_points += throw

    comp_throw = randint(1, comp_dice()) + randint(1, comp_dice())
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
