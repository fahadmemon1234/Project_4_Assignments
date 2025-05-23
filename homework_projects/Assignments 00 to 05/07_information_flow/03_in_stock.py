# -*- coding: utf-8 -*-
"""03_in_stock.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QvP9kgtxZ5HSqAd2oCfVnU456krozC42?usp=sharing
"""

fruit_inventory = {
    "apple": 50,
    "banana": 100,
    "orange": 2,
    "pear": 1000
}

def num_in_stock(fruit):
  return fruit_inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock}")
    else:
        print("This fruit is not in stock.")



if __name__ == '__main__':
    main()