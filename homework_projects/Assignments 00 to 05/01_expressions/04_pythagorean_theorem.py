# -*- coding: utf-8 -*-
"""04_pythagorean_theorem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hiAq63zPstGaL8GZptTF7OsVmC5h9G0F?usp=sharing
"""

import math  # Math library import kar raha hu taake sqrt function use kar sakun

def main():
     # User se do side lengths ka input le raha hu aur unhe number me convert kar raha hu
    abSide: float = float(input("Enter the length of AB: \033[1;3m"))
    acSide: float = float(input("\033[0mEnter the length of AC: \033[1;3m"))

     # Pythagoras Theorem ka use karke hypotenuse calculate kar raha hu
    bc: float = math.sqrt(abSide**2 + acSide**2)

     # Hypotenuse ki value print kar raha hu
    print("\033[0mThe length of BC (the hypotenuse) is: " + str(bc))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()