# -*- coding: utf-8 -*-
"""08_print_multiple.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nhJC5qVxvDl5mZk5RvJ-LFTs2tRHEVvF?usp=sharing
"""

CBLUE = '\33[34m'
CWHITE = '\33[37m'

def print_multiple(message, repeats):
    for i in range(repeats):
        print(f"{CWHITE}{message}", end=" ")



def main():
    message  = input(f"Please type a message: {CBLUE}")
    repeats = int(input(f"{CWHITE}Please type a number of repeats: {CBLUE}"))
    print_multiple(message, repeats)



if __name__ == '__main__':
    main()