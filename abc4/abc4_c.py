# -*- coding:utf-8 -*-

cards = [1, 2, 3, 4, 5, 6]
same = "".join(map(str, cards))
N = int(raw_input())

for i in range(N % 30):
    i_mod = i % 5
    tmp = cards[i_mod]
    cards[i_mod] = cards[i_mod + 1]
    cards[i_mod + 1] = tmp

print "".join(map(str, cards))
