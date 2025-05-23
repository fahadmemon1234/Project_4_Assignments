# -*- coding: utf-8 -*-
"""04_tall_enough_to_ride.ipynb

Automatically generated by Colab.

Original file is located at
   https://colab.research.google.com/drive/1Vn38lyHRbe-pzKBoXzZM3goaoA9z7BP8?usp=sharing
"""

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