## Problem Statement

Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high)
"""
Returns True if n is between low and high, inclusive.
high is guaranteed to be greater than low.
"""

## Solution

```bash


def in_range(n, low, high):
  if (n >= low and n <= high):
	  return True
  else:
	  return False


def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter low number: "))
    hight = int(input("Enter hight number: "))
    print(in_range(n, low, hight))


if __name__ == '__main__':
    main()



```
