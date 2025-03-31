## Problem Statement

Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]

## Solution

```bash
def main():
  number = [1,2,3,4,5]

  for i in range(len(number)):
    index_end = number[i]
    number[i] = index_end * 2

  print(number)



if __name__ == '__main__':
    main()
```
