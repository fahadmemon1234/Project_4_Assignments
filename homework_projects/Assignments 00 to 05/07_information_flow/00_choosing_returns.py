# -*- coding: utf-8 -*-
"""00_choosing_returns.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DFj7X9jLvKArZjhHHC61TZcRl7v3FWNy?usp=sharing
"""

bold_italic = "\033[1;3m"
reset = "\033[0m"

def is_adult(age):
  if (age >= 18):
    return True
  else:
    return False


def main():
  age = int(input(f"How old is this person?: {bold_italic}"))
  print(f"{reset}{is_adult(age)}")




if __name__ == '__main__':
    main()