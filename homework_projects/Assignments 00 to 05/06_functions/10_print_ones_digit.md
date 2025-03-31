## Problem Statement

Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Here's a sample run (user input is in blue):

Enter a number: 42
The ones digit is 2

## Solution

```bash
CBLUE = '\33[34m'
CWHITE = '\33[37m'

def print_ones_digit(num):
    ones_digit = num % 10
    print(f"{CWHITE}The ones digit is {ones_digit}")


def main():
    num = int(input(f"Enter a number: {CBLUE}"))
    print_ones_digit(num)



if __name__ == '__main__':
    main()

```
