# -*- coding:utf-8 -*-
import sys

R, C = map(int, raw_input().split())
sy, sx = map(lambda x: int(x) - 1, raw_input().split())
gy, gx = map(lambda x: int(x) - 1, raw_input().split())

status = [[-1 for i in range(C)] for j in range(R)]
meiro = []
for i in range(R):
    meiro.append(list(raw_input()))

status[sy][sx] = 0
queue = [[sy, sx]]

def calc_step(cur, step):
    global status, meiro, queue
    cury , curx = cur 
    for r in [-1, 1]:
        if (status[cury + r][curx] == -1) and (meiro[cury + r][curx] != '#'):
            status[cury + r][curx] = step
            queue.append([cury + r, curx])
    for c in [-1, 1]:
        if (status[cury][curx + c] == -1) and (meiro[cury][curx + c] != '#'):
            status[cury][curx + c] = step
            queue.append([cury, curx + c])   


if __name__ == '__main__':
    step = 1 
    while True:
        n_cur = len(queue)
        for i in range(n_cur):
            cur = queue.pop(0)
            if cur[0] == gy and cur[1] == gx:
                print status[cur[0]][cur[1]]
                sys.exit(0)
            calc_step(cur, step)
        step += 1

