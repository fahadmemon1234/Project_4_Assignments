# -*- coding: utf-8 -*-
"""04_multiple_returns.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bPsKyqbedr-K69M1NLoFbzto7Kj76KRr
"""

def get_user_data():
  firstname = input("What is your first name?: ")
  lastname = input("What is your last name?: ")
  email = input("What is your email address?: ")
  return f"Received the following user data: ('{firstname}', '{lastname}', '{email}')"


def main():
   userdata = get_user_data()
   print(userdata)



if __name__ == '__main__':
    main()