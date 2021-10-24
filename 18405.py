# 18405 경쟁적 전염
from collections import deque
n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])