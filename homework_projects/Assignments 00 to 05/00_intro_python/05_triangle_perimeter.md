## Problem Statement

Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5

## Solution

```bash
def main():
    # Get the 3 side lengths of the triangle

    # first-side length
    side1: float = float(input("What is the length of side 1? \033[1;3m"))
    # second-side length
    side2: float = float(input("\033[0mWhat is the length of side 2? \033[1;3m"))
    # third-side length
    side3: float = float(input("\033[0mWhat is the length of side 3? \033[1;3m"))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("\033[0mThe perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
```
