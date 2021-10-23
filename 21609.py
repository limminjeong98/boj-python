# 21609 상어중학교
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

def bfs(x, y, p):
    q.append([x, y])
    tmp = a[x][y]
    visited[x][y] = p
    cnt, r = 1, 0
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if a[nx][ny] == tmp and visited[nx][ny] == 0:
                visited[nx][ny] = p
                cnt += 1
                q.append([nx, ny])
            elif a[nx][ny] == 0 and p not in visited[nx][ny]:
                visited[nx][ny].append(p)
                cnt += 1
                r += 1
                q.append([nx, ny])
    return cnt, r

def fall(x, y):
    flag = False
    for i in range(x + 1, n):
        nx = i
        if a[i][y] > -2:
            flag = True
            break
    if flag:
        a[nx - 1][y] = a[x][y]
    else:
        a[nx][y] = a[x][y]
    a[x][y] = -2

while True:
    q = deque()
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                visited[i][j] = []
    p, b = 1, []
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0 and visited[i][j] == 0:
                cnt, r = bfs(i, j, p)
                if cnt > 1:
                    b.append([cnt, r, i, j, p])
                p += 1
    if not b:
        break

    b = sorted(b)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0 and visited[i][j] == b[-1][-1]:
                a[i][j] = -2
                cnt += 1
            elif a[i][j] == 0 and b[-1][-1] in visited[i][j]:
                a[i][j] = -2
                cnt += 1
    answer += cnt ** 2

    for i in range(n - 2, -1, -1):
        for j in range(n):
            if a[i][j] >= 0 and a[i + 1][j] == -2:
                fall(i, j)

    a = list(zip(*a))[::-1]
    a = [list(s) for s in a]

    for i in range(n - 2, -1, -1):
        for j in range(n):
            if a[i][j] >= 0 and a[i + 1][j] == -2:
                fall(i, j)

print(answer)