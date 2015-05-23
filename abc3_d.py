# -*- coding:utf-8 -*-
import sys
from math import factorial as fact

def comb(n, k):
    if n < k:
        return 0
    return fact(n) / (fact(k) * fact(n - k))

first = raw_input()
second = raw_input()
third = raw_input()

divisor = pow(10, 9) + 7

row = int(first.split(" ")[0])
col = int(first.split(" ")[1])
x = int(second.split(" ")[0])
y = int(second.split(" ")[1])
desk = int(third.split(" ")[0])
rack = int(third.split(" ")[1])

deploy = (row - x + 1) * (col - y + 1)
if x * y == desk + rack:
    desk_comb = comb(x * y, desk)
    rack_comb = comb(x * y -desk, rack) 
    print (deploy * desk_comb * rack_comb) % divisor
    sys.exit()

all_comb = comb(x * y, desk + rack)

top = comb((x - 1) * y, desk + rack)
bottom = comb((x - 1) * y, desk + rack)
left = comb(x * (y - 1), desk + rack)
right = comb(x * (y - 1), desk + rack)
one_except = top + bottom + left + right

top_bottom = comb((x - 2) * y, desk + rack)
top_left = comb((x - 1) * (y - 1), desk + rack)
top_right = comb((x - 1) * (y - 1), desk + rack)
bottom_left = comb((x - 1) * (y - 1), desk + rack)
bottom_right = comb((x - 1) * (y - 1), desk + rack)
left_right = comb(x * (y - 2), desk + rack)
two_except = top_bottom + top_left + top_right + bottom_left + bottom_right + left_right

top_bottom_left = comb((x - 2) * (y - 1), desk + rack)
top_bottom_right = comb((x - 2) * (y - 1), desk + rack)
top_left_right = comb((x - 1) * (y - 2), desk + rack)
bottom_left_right = comb((x - 1) * (y - 2), desk + rack)
three_except = top_bottom_left + top_bottom_right + top_left_right + bottom_left_right

top_bottom_left_right = comb((x - 2) * (y - 2), desk + rack)

all_except =  one_except - two_except + three_except - top_bottom_left_right 
print deploy * (all_comb - all_except) * comb(desk + rack, desk) % divisor
