## Problem Statement

This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3
Enter a number: 4
Enter a number: 3
Enter a number: 6
Enter a number: 4
Enter a number: 3
Enter a number: 12
Enter a number: 
3 appears 3 times.
4 appears 2 times.
6 appears 1 times.
12 appears 1 times.

## Solution

```bash
CBLUE = '\33[34m'
CWHITE = '\33[37m'


def main():
    user_list = []

    while True:
      num = input(f"{CWHITE}Enter a number: {CBLUE}")

      if (num == ""):
        break
      user_list.append(int(num))

    frequency = {}

    for num in user_list:
      if num in frequency:
        frequency[num] += 1
      else:
        frequency[num] = 1

    for num, count in frequency.items():
      print(f"{CWHITE}{num} appears {count} times.")
          
        
if __name__ == '__main__':
    main()
```