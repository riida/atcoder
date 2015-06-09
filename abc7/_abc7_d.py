# -*- coding:utf-8 -*-

def solve(n):
    L = len(str(n))
    dp = [[0 for i in range(2)] for j in range(20)]
    digit = [0 for i in range(20)]
    size = 0
    while(n):
        digit[size] = n % 10
        n /= 10
        size += 1

    dp[0][1] = 1
    for i in range(L):
        d = digit[(L - 1) - i]
        for j in range(0, 10):
            if (j != 4 and j != 9):
                if (j < d):
                    dp[i + 1][0] += (dp[i][0] + dp[i][1])
                if (j == d):
                    dp[i + 1][1] += dp[i][1]
                    dp[i + 1][0] += dp[i][0]
                if (j > d):
                    dp[i + 1][0] += dp[i][0]
            print dp


if __name__ == '__main__':
    A, B = map(int, raw_input().split(" "))
    solve(A)
