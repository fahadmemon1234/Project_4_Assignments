# -*- coding: utf-8 -*-
"""Project1 _Mad_libs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/159FdfE1niwIBnpngL-eXZqZP8BCKnxjp?usp=sharing
"""

name = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion (like happy, angry): ")
verb = input("Enter a verb (action word like run, think): ")

story = f"""
One day, {name} went to {place}.
There, they saw a {animal}, and it looked very {emotion}.
{name} thought it was a good idea to {verb}.
And then, they both had a great time together!
"""

print("\nHere is your Mad Libs story: ")
print(story)