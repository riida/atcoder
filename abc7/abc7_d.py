# -*- coding:utf-8 -*-
import sys

A, B = map(int, raw_input().split())

def ban_counter(n):

    if n == 0: return 0
    n_length = len(str(n))
    digit = [0 for i in range(n_length)]
    store = [[0 for i in range(2)] for i in range(20)]# 10**iに4と9を含む数字がいくつ含まれるか
    index = 0
    while n:
        digit[index] = n % 10
        n /= 10
        index += 1

    for i in range(n_length):
        res_count = 0
        store_count = 0
        for j in range(10):
            if (j == 4) or (j == 9):
                store_count += 10 ** i
                if (j < digit[i]):
                    res_count += 10 ** i
                elif (j == digit[i]):
                    rest = 1
                    for n_dig in range(i):
                        rest += (10 ** n_dig) * digit[n_dig]
                    res_count += rest
                    store[i + 1][1] = res_count
            else:
                store_count += store[i][0]
                if (j < digit[i]):
                    res_count += store[i][0]
                elif (j == digit[i]):
                    res_count += store[i][1] 
                    store[i + 1][1] = res_count
        store[i + 1][0] = store_count
    return store[n_length][1]

print ban_counter(B) - ban_counter(A - 1)
