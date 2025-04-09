# -*- coding: utf-8 -*-
"""03_powerful_passwords.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AcadnZ5qLKzOcy91Atu_-UklWeLGhpL7?usp=sharing
"""

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com": hash_password("mypassword123"),
    "test@example.com": hash_password("hello123"),
    "admin@example.com": hash_password("adminpass")
}

def login(email, password_to_check):
  if email not in stored_logins:
    return False

  hashed_input_password = hash_password(password_to_check)
  return stored_logins[email] == hashed_input_password

def main():
  email = input("Enter your email: ")
  password = input("Enter your password: ")

  if login(email, password):
    print("✅ Login successful!")
  else:
    print("❌ Incorrect email or password!")





if __name__ == '__main__':
    main()