# 16236 아기상어
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maps = []
for _ in range(n):
    maps.append(list(map(int, input().rstrip().split())))

s_x, s_y = 0, 0
time = 0
size = 2
ate = 0

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            s_x, s_y = i, j
            maps[i][j] = 0

# 상어가 도달할 수 있는 물고기들의 거리를 구하는 함수
def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[s_x][s_y] = 0
    q = deque([(s_x, s_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 아직 방문하지 않은 위치이고 상어가 지나갈 수 있는 위치
                if dist[nx][ny] == -1 and maps[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

# 먹을 물고기를 찾는 함수
def find_fish(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if 0 < maps[i][j] < size and dist[i][j] != -1:
                if min_dist > dist[i][j]:
                    min_dist = dist[i][j]
                    x, y = i, j
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist
    

while True:
    result = find_fish(bfs())
    if result == None:
        print(time)
        break
    else:
        s_x, s_y = result[0], result[1]
        time += result[2]
        maps[s_x][s_y] = 0
        ate += 1
        if ate >= size:
            size += 1
            ate = 0