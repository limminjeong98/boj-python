# 14503 로봇 청소기
from collections import deque
import sys
# 런타임에러 해결
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# 세로 n 가로 m
n, m = map(int, input().rstrip().split(' '))
r, c, d = map(int, input().rstrip().split(' '))
# r -= 1
# c -= 1

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().rstrip().split(' ')))

# 북(0) 동(1) 남(2) 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

visited = [[False] * m for _ in range(n)]


def rotate(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


def bfs(arr, r, c, d):
    q = deque([(r, c, d)])
    # 처음은 무조건 빈 칸
    total = 1
    while q:
        x, y, d = q.popleft()
        visited[x][y] = True
        found = False
        for k in range(4):
            if found:
                break
            # 현재 방향 d 기준으로 왼쪽 방향부터 탐색
            d = rotate(d)
            nx, ny = x + dx[d], y + dy[d]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if visited[nx][ny] or arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                q.append((nx, ny, d))
                total += 1
                found = True
                break
        if found:
            continue
        # 네 방향 모두 청소가 되어있거나, 벽인 경우에는 방향을 유지한 채로 한 칸 후진
        nx, ny = x - dx[d], y - dy[d]
        # 뒤쪽 방향이 벽이거나 후진 불가능하면 종료
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            return total
        if arr[nx][ny] == 1:
            return total
        q.append((nx, ny, d))
        # 처음 청소하는 칸일 때만 체크
        if not visited[nx][ny]:
            total += 1
    return total


result = bfs(arr, r, c, d)

print(result)
