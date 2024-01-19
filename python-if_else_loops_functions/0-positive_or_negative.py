#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=' ')
print("is positive" if number > 0
      else "is zero" if number == 0 else "is negative")
