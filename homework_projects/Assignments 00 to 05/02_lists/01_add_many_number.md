## Problem Statement

Write a function that takes a list of numbers and returns the sum of those numbers.

## Solution

```bash
def add_numbers(numbers):
  total = 0
  for i in numbers:
    total += i
  return total


def main():
   numbers = [1, 2, 3, 4, 5]
   result = add_numbers(numbers)
   print(result)

if __name__ == '__main__':
    main()
```
