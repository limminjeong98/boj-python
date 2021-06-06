from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline
n, q = map(int, input().split())
tn = 2 ** n
maps = []
for i in range(tn):
    maps.append(list(map(int, input().split())))
step = list(map(int, input().split()))
rem = 0
maxIce = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate_right(table, tl):
    tbl = [[0] * tl for _ in range(tl)]
    for i in range(tl):
        for j in range(tl):
            tbl[j][tl-i-1] = table[i][j]
    return tbl

def check():
    new_maps = deepcopy(maps)
    for i in range(tn):
        for j in range(tn):
            cnt = 0
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < tn and 0 <= nj < tn:
                    if maps[ni][nj] > 0:
                        cnt += 1
            if new_maps[i][j] > 0 and cnt < 3:
                new_maps[i][j] -= 1
    return new_maps    

def bfs(x, y):
    global visited
    global maxIce
    visited[x][y] = True
    q = deque([(x, y)])
    cnt = 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            cx, cy = nx + dx[i], ny + dy[i]
            if 0 <= cx < tn and 0 <= cy < tn:
                if visited[cx][cy] == False:
                    visited[cx][cy] = True
                    if maps[cx][cy] > 0:
                        cnt += 1
                        q.append([cx, cy])
    maxIce = max(maxIce, cnt)


for i in range(q):
    l = step[i]
    tl = 2 ** l
    x_start, y_start = 0, 0
    for x in range(x_start, tn, tl):
        for y in range(y_start, tn, tl):
            tmp = [[0] * tl for _ in range(tl)]
            for r in range(tl):
                for c in range(tl):
                    tmp[r][c] = maps[x+r][y+c]
        
            tmp = rotate_right(tmp, tl)
            for r in range(tl):
                for c in range(tl):
                    maps[x+r][y+c] = tmp[r][c]
    maps = check()
    

visited = [[False] * tn for _ in range(tn)]
for x in range(tn):
    for y in range(tn):
        rem += maps[x][y]
        if visited[x][y] == False and maps[x][y] > 0:
            bfs(x, y)

print(rem)
if maxIce < 2:
    print(0)
else:
    print(maxIce)

