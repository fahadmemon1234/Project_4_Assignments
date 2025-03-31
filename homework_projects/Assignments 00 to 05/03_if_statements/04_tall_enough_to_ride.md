## Problem Statement

Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

Here's two sample runs (user input is in bold italics):

How tall are you? 100 

You're tall enough to ride!

How tall are you? 10 

You're not tall enough to ride, but maybe next year!

(For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

## Solution

```bash
minimum_height = 50

def main():
    
  while True:
      height_input = input("How tall are you? \033[1;3m")

      if (height_input == ""):
        print("\033[0mExiting the program. Have a great day!")
        break

      try:
        height = int(height_input)
      except ValueError:
        print("\033[0mPlease enter a valid number.")
        continue

      if(height >= minimum_height):
        print("\033[0mYou're tall enough to ride!")
      else:
        print("\033[0mYou're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()
```
