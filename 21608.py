n = int(input())
arr = [[] * 4 for _ in range(n**2)]
maps = [[-1] * n for _ in range(n)]
data = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n**2):
    tmp = list(map(int, input().split()))
    arr[tmp[0]-1] = tmp[1:]
    data.append(tmp[0]-1)

ans = 0

def count_like(x, y, likes):
    cnt = 0
    blank = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == -1:
                blank += 1
            if maps[nx][ny] in likes:
                cnt += 1
    return cnt, blank

def find_best(likes):
    x, y, cnt, blank = -1, -1, 0, 0
    tmpcnt, tmpblank = 0, 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == -1:
                if x == -1 and y == -1:
                    x, y = i, j
                tmpcnt, tmpblank = count_like(i, j, likes)
                if cnt < tmpcnt:
                    cnt = tmpcnt
                    blank = tmpblank
                    x, y = i, j
                elif cnt == tmpcnt:
                    if blank < tmpblank:
                        blank = tmpblank
                        x, y = i, j      
    return x, y


for s in data:
    likes = arr[s]
    x, y = find_best(likes)
    maps[x][y] = s + 1
    
for x in range(n):
    for y in range(n):
        cnt = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] in arr[maps[x][y]-1]:
                    cnt += 1
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)