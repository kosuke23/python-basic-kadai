# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmWFa5DeuiZPM-GfFfn_i10EnfHQGlRa
"""

import random

var = random.randint(1, 30)

print(var)


if var % 15 == 0:
    print("FizzBuzz")
elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else:
    print("var")
