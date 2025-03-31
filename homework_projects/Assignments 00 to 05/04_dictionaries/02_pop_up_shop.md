## Problem Statement

There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs. 

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5

## Solution

```bash
def main():
    fruits = {'apple': 10, 'durian': 5, 'jackfruit': 56, 'kiwi': 100, 'rambutan': 33, 'mango': 1.5}

    total_cost = 0 
    
    for fruit_name in fruits:
        price = fruits[fruit_name]
        try:
            amount_bought = int(input(f"\033[0mHow many ({fruit_name}) do you want to buy?: \033[1;3m"))
            total_cost += (price * amount_bought)
        except ValueError:
            print("\033[0mInvalid input! Please enter a valid number.")

   
    print(f"\033[0mYour total is ${total_cost}")


if __name__ == '__main__':
    main()

```
