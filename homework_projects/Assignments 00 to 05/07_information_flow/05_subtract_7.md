## Problem Statement

Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

## Solution

```bash
def subtract_seven(num):
  return num - 7


def main():
  num = int(input("Enter a number: "))
  result = subtract_seven(num)
  print("this should be zero:", result)




if __name__ == '__main__':
    main()
```
