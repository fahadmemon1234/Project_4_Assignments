## Problem Statement

Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

Here's a sample run (user input is in blue):

Enter a number: 12
Here are the divisors of 12
1
2
3
4
6
12

## Solution

```bash
CBLUE = '\33[34m'
CWHITE = '\33[37m'

def print_divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


def main():

    num = int(input(f"Enter a number: {CBLUE}"))
    print(f"{CWHITE}The divisors of", num, "are:")
    print_divisors(num)



if __name__ == '__main__':
    main()
```
