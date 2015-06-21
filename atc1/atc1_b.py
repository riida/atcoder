# -*- coding:utf-8 -*-

N, Q = map(int, raw_input().split())
parents = range(N)

def root(x):

    if parents[x] == x:
        return x
    parents[x] = root(parents[x])
    return parents[x]

def connect(A, B):
    global parents
    if ((A == B) or (root(A) == root(B))): return
    parents[root(B)] = root(A)
    return

def judge(A, B):
    global parents
    if (A == B) or (root(A) == root(B)):
        print 'Yes'
    else:
        print 'No'
    return

for i in range(Q):

    P, A, B = map(int, raw_input().split())
    if (P == 0): connect(A, B)  
    if (P == 1): judge(A, B)
