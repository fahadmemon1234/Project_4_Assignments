## Problem Statement

Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

Here's a sample run of the program (user input in bold italics):

Enter a number: 2
Double that is 4

## Solution

```bash

bold_italic = "\033[1;3m"
reset = "\033[0;0m"

def double(num):
  return num * 2

def main():

  num = int(input(f"Enter a number: {bold_italic}"))

  total = double(num)

  print(f"{reset}{num} Double that is {total}.")




if __name__ == '__main__':
    main()
```
