## Problem Statement

Simulate rolling two dice, and prints results of each roll as well as the total.

## Starter Code

```bash
def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
```

## Solution

```bash
def main():
    import random

    NUM_SIDES: int = 6

    die1: int = random.randrange(1, NUM_SIDES + 1)
    die2: int = random.randrange(1, NUM_SIDES + 1)

    total = die1 + die2

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First Dice No {die1}")
    print(f"Second Dice No {die2}")
    print(f"Your total is {total}.")


if __name__ == '__main__':
    main()

```
