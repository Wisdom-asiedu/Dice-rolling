import random

def roll_dice(num_dice, num_sides):
    rolls = []
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        total += roll
    print("Roll results:", rolls)
    print("Total score:", total)

def validate_input():
    num_dice = int(input("Enter the number of dice to roll: "))
    if num_dice > 0:
        num_sides = int(input("Enter the number of sides for each die: "))
        if num_sides > 0:
            roll_dice(num_dice, num_sides)
        else:
            print("The number on a die should be countable")
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

if __name__ == "__main__":
    main()
