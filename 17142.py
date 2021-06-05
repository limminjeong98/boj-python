from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maps = []
visited = [[False] * n for _ in range(n)]
test_visited = [[False] * n for _ in range(n)]
virus = []
active = []
blank = False
for _ in range(n):
    maps.append(list(map(int, input().split())))
test_maps = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = -1
        elif maps[i][j] == 2:
            maps[i][j] = -2
            virus.append((i, j))

v = len(virus)
ans = int(1e9)
flag = False

def dfs(cnt, idx):
    global flag, ans
    local_ans = 0
    if cnt == m:
        for i in range(n):
            for j in range(n):
                test_maps[i][j] = maps[i][j]
                test_visited[i][j] = visited[i][j]
        for x, y, cur_time in active:
            test_visited[x][y] = True
        q = deque(active)
        while q:
            x, y, cur_time = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not test_visited[nx][ny]:
                    test_visited[nx][ny] = True
                    if test_maps[nx][ny] == 0:
                        test_maps[nx][ny] = cur_time + 1
                        q.append((nx, ny, test_maps[nx][ny]))
                    elif test_maps[nx][ny] == -2:
                        q.append((nx, ny, cur_time + 1)) 

        for i in range(n):
            for j in range(n):
                if test_maps[i][j] == 0:
                    return
                if local_ans < test_maps[i][j]:
                    local_ans = test_maps[i][j]

        flag = True
        ans = min(ans, local_ans)
        return
    
    for i in range(idx, v):
        active.append((virus[i][0], virus[i][1], 0))
        dfs(cnt+1, i+1)
        active.pop()
        
for i in range(n):
    for j in range(n):
        if maps[i][j] == 0 and not blank:
            blank = True
if not blank:
    print(0)
else:
    dfs(0, 0)
    if not flag:
        print(-1)
    else:
        print(ans)