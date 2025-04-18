# -*- coding: utf-8 -*-
"""00_count_nums.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ngiuMCmwIdCAuX79LTBAm7MITZtf0OJ5?usp=sharing
"""

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