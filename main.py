import re
from random import randint

def dice(code):
    """
    Dice roll.
    User input which type of dice he want to throw.
    :param code: xDy+z  where: x = throws, Dy = type of dice, z = additional modifier ex. '2D10+10'
    :rtype: int
    :return: Function returns the result of two throws of the chosen dice.
    """
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    throws = 2
    valid_dice = 0
    result = 0
    found_dice = re.findall(r"D\d+", code)[0]
    while found_dice in dice_types:
        try:
            valid_dice = int(found_dice[1::])
        except IndexError:
            print("Invalid code")
        except TypeError:
            print("Invalid code")
        for x in range(throws):
            result += randint(1, valid_dice)
        return result
    if found_dice not in dice_types:
        return "Invalid dice type"


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

