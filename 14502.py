# 14502 연구소
n, m = map(int, input().split())
arr = []
blank = []
virus = []

for i in range(n):
    arr.append(list(map(int, input().split())))

tmp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def virus(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        if tmp[nx][ny] == 0:
            tmp[nx][ny] = 2
            virus(nx, ny)

def get_score():
    total = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                total += 1
    return total

def dfs(cnt):
    global answer
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = arr[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        answer = max(answer, get_score())
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(cnt + 1)
                arr[i][j] = 0

dfs(0)
print(answer)