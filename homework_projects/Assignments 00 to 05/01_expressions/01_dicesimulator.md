## Problem Statement

Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

## Starter Code

```bash
# Random library ko import kar rahe hain jo humein dice ka random number generate karne deta hai.
import random

# Har dice ke total sides (yahan hum 6-sided dice use kar rahe hain).
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    dice1: int = 10
    print("die1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(dice1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
```
