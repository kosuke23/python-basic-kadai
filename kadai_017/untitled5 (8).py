# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmWFa5DeuiZPM-GfFfn_i10EnfHQGlRa
"""

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print("大人")
        else:
            print("大人でない")

data = [["太郎", 10],
        ["二郎", 15],
        ["三郎", 20],
        ["四郎", 30],
        ["五郎", 40]]

human_info = []
for d in data:
    human_info.append((d[0], d[1]))

for h in human_info:
    Human(h[0], h[1]).check_adult()

