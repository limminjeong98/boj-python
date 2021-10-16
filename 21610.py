# 21610 마법사 상어와 비바라기
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = []
for i in range(n):
    a.append(list(map(int, input().rstrip().split())))

# 8개의 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향으로 거리가 1인 칸
ox = [-1, 1, -1, 1]
oy = [-1, -1, 1, 1]

moves = []
for i in range(m):
    d, s = map(int, input().split())
    moves.append((d-1, s))

answer = 0

# 비바라기를 시전하면 칸에 구름이 생긴
cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

for w in range(m):
    new_cloud = []
    d, s = moves[w]
    length = len(cloud)
    # 모든 구름이 d 방향으로 s칸 이동
    for i in range(length):
        cx = (cloud[i][0] + dx[d] * s) % n
        cy = (cloud[i][1] + dy[d] * s) % n
        cloud[i] = (cx, cy)
        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양 1 증가
        a[cx][cy] += 1
    # 물이 증가한 칸에 물복사버그 마법
    # 대각선으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 바구니의 물의 양이 증가
    for i in range(length):
        x, y = cloud[i]
        cnt = 0
        for d in range(4):
            nx, ny = x + ox[d], y + oy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] > 0:
                    cnt += 1
        a[x][y] += cnt
    # 바구니에 저장된 물의 양이 2이상인 칸에 구름이 새로 생김
    # 이때 이전에 구름이 사라진 칸이 아니어야 함
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2:
                if (i, j) not in cloud:
                    a[i][j] -= 2
                    new_cloud.append((i, j))
    cloud = new_cloud
                
for i in range(n):
    for j in range(n):
        answer += a[i][j]
print(answer)