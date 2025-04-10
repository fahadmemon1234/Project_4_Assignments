# -*- coding: utf-8 -*-
"""03_feet_to_inches.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1opsJ9qPb90wkqJtXDLj8Re3iCkMtgDdS?usp=sharing
"""

INCHES_IN_FOOT: int = 12  # Conversion factor: 1 foot = 12 inches

def main():
    feet: float = float(input("Enter number of feet: "))  # User se input le raha hu (feet me) cast for float
    inches: float = feet * INCHES_IN_FOOT  # Feet ko inches me convert kar raha hu
    # Result show kar raha hu
    print("That is", inches, "inches!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()