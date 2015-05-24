# -*- coding:utf-8 -*-
import math
R, G, B = map(int, raw_input().split(" "))

def step(n):
    ceil = int(math.ceil(n / 2.0))
    floor = int(math.floor(n / 2.0))
    return sum(range(ceil + 1)) + sum(range(floor + 1))

if R * 
    R + G + B < 202:
    G_ceil = int(math.ceil(G / 2.0))
    G_floor = int(math.floor(G / 2.0))
print step(R - 1) + step(G - 1) + step(B - 1)
