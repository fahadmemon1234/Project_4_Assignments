# -*- coding: utf-8 -*-
"""Binary_Search_Python_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eDsxmH3K6Kc7OXNqUKOw12MQOQra9AxR?usp=sharing
"""

def binary_search(arr, low, high, target):
  if(high >= low):
    mid = low + (high - low) // 2
    if(arr[mid] == target):
      return mid
    elif(arr[mid] > target):
      return binary_search(arr, low, mid - 1, target)
    else:
      return binary_search(arr, mid + 1, high, target)
  else:
    return -1



arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the number to search: "))

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")