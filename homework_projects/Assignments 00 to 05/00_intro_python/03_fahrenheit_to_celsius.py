# -*- coding: utf-8 -*-
"""03_fahrenheit_to_celsius.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gv4T6XKazuX0CJIPD5o3e9Yz5XDtNFdH?usp=sharing
"""

def main():

    # Step 1: user se input
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: \033[1;3m"))

    # Step 2: convert krdiya hai celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Step 3: print krdiya hai
    print(f"\033[0mTemperature: {degrees_fahrenheit}F = {degrees_celsius}C")


if __name__ == '__main__':
    main()