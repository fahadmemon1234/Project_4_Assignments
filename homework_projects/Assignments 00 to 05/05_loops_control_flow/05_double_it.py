# -*- coding: utf-8 -*-
"""05_double_it.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iqc3ju8oJTKQZo9df_ypAi1spi90Fv38
"""

def main():

    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
      curr_value *= 2
      print(curr_value, end=" ")



if __name__ == '__main__':
    main()