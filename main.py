import random
from mod.dice_art import dice_art as dice

def roll_dice(num_dice: int, num_sides: int) -> None:
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        total = sum(rolls)

    # Displays dice art for 9 sided-die. The number of dice depends on the width of your screen to prevent
    # distortion of the art. It could be adjusted accordingly to fill the width of the terminam
    if num_dice <= 12 and num_sides <= 9:               # Adjust num-dice to fill the width of your terminal
        for line in range(5):
            for roll in rolls:
                print(dice.get(roll)[line], end="")
            print()
    else:
        pass
    # Outputs rresult
    print("Roll results:", rolls)
    print("Total score:", total)

def validate_input() -> None:
    num_dice = int(input("Enter the number of dice to roll: "))
    if num_dice > 0:
        num_sides = int(input("Enter the number of sides for each die: "))
        if num_sides > 0:
            roll_dice(num_dice, num_sides)
        else:
            print("Cannot roll a die without sides")
    else:
        print("The number of dice should be countable")

def main():
    print("---Welcome to the Dice Rolling Simulator!---")
    while True:
        try:
            validate_input()
        
            while True:
                choice = input("\nRoll again? (y/n): ")
                if choice.lower() == 'y':
                    print()
                    break
                elif choice.lower() == 'n':
                    print("Thanks for playing!")
                    quit()
                else:
                    pass
        except ValueError:
            print("Enter a counting number!\n")

# Calls the main function
if __name__ == "__main__":
    main()
