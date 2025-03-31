## Problem Statement

Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2

## Solution

```bash
def main():
  # User se ek integer input le raha hu jo divide hoga
  dividing: int = int(input("Please enter an integer to be divided: \033[1;3m"))
  # User se ek integer input le raha hu jo divisor hoga
  divisor: int = int(input("Please enter an integer to divide by: \033[1;3m"))

  # Quotient nikal raha hu (dividing ko divisor se divide kar ke)
  quotient: int = dividing // divisor

  # Remainder nikal raha hu (dividing ka divisor se bachne wala hissa)
  remainder: int = dividing % divisor

  # Result ko print kar raha hu
  print("\033[0mThe result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()
```
