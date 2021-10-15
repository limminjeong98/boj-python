# 16234 인구 이동
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

def move(x, y, idx):
    united = []
    average = 0
    union[x][y] = idx
    total = arr[x][y]
    # 새로운 연합을 생성
    united.append((x, y))
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    union[nx][ny] = idx
                    united.append((nx, ny))
                    q.append((nx, ny))
                    total += arr[nx][ny]
    average = total // len(united)
    for i, j in united:
        arr[i][j] = average
                    
cnt = 0        
while True:
    idx = 0
    union = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                move(i, j, idx)
                idx += 1
    if idx == n * n:
        break
    cnt += 1
print(cnt)