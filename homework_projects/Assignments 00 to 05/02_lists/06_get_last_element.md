## Problem Statement

Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

## Starter Code

```bash
# Pehla element lene ka function
def get_first_element(lst):
  print(lst[-1]) # List ka Last element print karega


# User se list lene ka function
def get_list():
  lst = [] # Khali list banayenge
  userValue = input("Please enter an element of the list or press enter to stop. ")
  while userValue != "": # Jab tak user enter na dabaye, values list me add hoti rahengi
    lst.append(userValue)
    userValue = input("Please enter an element of the list or press enter to stop. ")
  return lst # Puri list return karega

# Main function jo sab kuch control karega
def main():
  lst = get_list()
  get_first_element(lst)



if __name__ == '__main__':
    main()
```
