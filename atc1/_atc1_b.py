# -*- coding:utf-8 -*-

N, Q = map(int, raw_input().split())
#nodes = [0 for i in range(N)]
nodes = range(N)

def connect(A, B):
    global nodes
    if ((A == B) or (nodes[A] == nodes[B])): return
    if (nodes[A] < nodes[B]):
        small = A
        large = B
    else:
        small = B
        large = A

    nodes[large] = nodes[small]
    return

def judge(A, B):
    global nodes
    if (A == B) or (nodes[A] == nodes[B]):
        print 'Yes'
    else:
        print 'No'
    
    return

for i in range(Q):

    P, A, B = map(int, raw_input().split())
    if (P == 0): connect(A, B)  
    if (P == 1): judge(A, B)
