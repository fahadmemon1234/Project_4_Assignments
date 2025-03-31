## Problem Statement

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

1. Prompt the user to enter the first number.

2. Read the input and convert it to an integer.

3. Prompt the user to enter the second number.

4. Read the input and convert it to an integer.

5. Calculate the sum of the two numbers.

6. Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

## Solution

```bash

def main():
    print("This program adds two numbers.")
    # user input first number
    firstNumber : str = input("Enter first number: ")
    # (firstNumber) convert to INT
    firstNumber : int = int(firstNumber)

    # user input second number
    secondNumber  : str = input("Enter second number: ")

    # (secondNumber) convert to INT
    secondNumber : int = int(secondNumber)

    # (firstNumber + secondNumber) sum two number2
    total : int = firstNumber + secondNumber

    # print the total number and display the terminal
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
```
