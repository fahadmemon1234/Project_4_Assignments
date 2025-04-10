# -*- coding: utf-8 -*-
"""08_shorten.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dQJM9P8S58S71VFAymsuSJzJGqkVhbyY?usp=sharing
"""

MAX_LENGTH = 3

def shorten(lst):
  while len(lst) > MAX_LENGTH:
    last_elem = lst.pop()
    print(last_elem)

def get_lst():
  lst = []
  value = input("Please enter an element of the list or press enter to stop. ")
  while value != "":
    lst.append(value)
    value = input("Please enter an element of the list or press enter to stop. ")
  return lst

def main():
  lst = get_lst()
  shorten(lst)




if __name__ == '__main__':
    main()