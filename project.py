import random

def roll_dice(num_dice, num_sides):
    rolls = []
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        total += roll
    return rolls, total

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides for each die: "))
        
        rolls, total = roll_dice(num_dice, num_sides)
        
        print("Roll results:", rolls)
        print("Total score:", total, '\n')
        
        choice = input("Roll again? (y/n): ")
        if choice.lower() == 'y':
            pass
        elif choice.lower() == 'n':
            print("Thanks for playing!")
            break 

if __name__ == "__main__":
    main()
