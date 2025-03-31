## Problem Statement

Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

Here's a sample run of the program (user input is in blue):

How old are you? 20 
You can vote in Peturksbouipo where the voting age is 16. 
You cannot vote in Stanlau where the voting age is 25. 
You cannot vote in Mayengua where the voting age is 48.

## Solution

```bash

CBLUE = '\33[34m'
CWHITE = '\33[37m'

def main():
    Peturksbouipo_age = 16
    Stanlau_age = 25
    Mayengua_age = 48

    user_input = int(input(f"How old are you? {CBLUE}"))

    if(user_input >= Peturksbouipo_age):
      print(f"{CWHITE}You can vote in Peturksbouipo where the voting age is {Peturksbouipo_age}.")
    else:
      print(f"{CWHITE}You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo_age}.")


    if(user_input >= Stanlau_age):
      print(f"{CWHITE}You can vote in Stanlau where the voting age is {Stanlau_age}.")
    else:
      print(f"{CWHITE}You cannot vote in Stanlau where the voting age is {Stanlau_age}.")  

    if(user_input >= Mayengua_age):
      print(f"{CWHITE}You can vote in Mayengua where the voting age is {Mayengua_age}.")
    else:
      print(f"{CWHITE}You cannot vote in Mayengua where the voting age is {Mayengua_age}.")

if __name__ == '__main__':
    main()
```