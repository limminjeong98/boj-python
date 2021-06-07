import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ox = [-1, 1, -1, 1]
oy = [-1, -1, 1, 1]
moves = []
for i in range(m):
    d, s = map(int, input().split())
    moves.append((d-1, s))
ans = 0

cloud = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]

for w in range(m):
    new_cloud = []
    d, s = moves[w]
    length = len(cloud)
    for i in range(length):
        cx = (cloud[i][0] + dx[d] * s) % n
        cy = (cloud[i][1] + dy[d] * s) % n
        cloud[i] = (cx, cy)
        a[cx][cy] += 1
    for i in range(length):
        x, y = cloud[i]
        cnt = 0
        for d in range(4):
            nx, ny = x + ox[d], y + oy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] > 0:
                    cnt += 1
        a[x][y] += cnt

    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2:
                if (i, j) not in cloud:
                    a[i][j] -= 2
                    new_cloud.append((i, j))
    cloud = new_cloud
                
for i in range(n):
    for j in range(n):
        ans += a[i][j]
print(ans, end='')