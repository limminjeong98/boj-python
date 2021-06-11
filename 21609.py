from collections import deque
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def bfs(x, y):
    base_x, base_y = x, y
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    cnt, rainbow = 1, 0
    q = deque([(x, y)])
    num = maps[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if maps[nx][ny] == num:
                    cnt += 1
                    q.append((nx, ny))
                    if nx < base_x and ny < base_y:
                        base_x, base_y = nx, ny
                elif maps[nx][ny] == 0:
                    rainbow += 1
                    cnt += 1
                    q.append((nx, ny))
    return cnt, rainbow, base_x, base_y

def find_group():
    cnt, tmpcnt = 1, 0
    cx, cy = 0, 0
    base_x, base_y = -1, -1
    rainbow, tmprainbow = -1, 0
    for x in range(n-1, -1, -1):
        for y in range(n-1, -1, -1):
            if maps[x][y] > 0:
                tmpcnt, tmprainbow, tmp_base_x, tmp_base_y = bfs(x, y)
                if tmpcnt > cnt:
                    cnt = tmpcnt
                    cx, cy = x, y
                    rainbow = tmprainbow
                    base_x, base_y = tmp_base_x, tmp_base_y
                elif tmpcnt == cnt:
                    if tmprainbow > rainbow:
                        cx, cy = x, y
                        rainbow = tmprainbow
                        base_x, base_y = tmp_base_x, tmp_base_y
                        if tmprainbow == rainbow:
                            if tmp_base_x > base_x:
                                cx, cy = x, y
                                base_x, base_y = tmp_base_x, tmp_base_y
                            elif tmp_base_x == base_x:
                                if tmp_base_y > base_y:
                                    cx, cy = x, y
                                    base_x, base_y = tmp_base_x, tmp_base_y


    if cnt == 1:
        return None
    return cnt, cx, cy

def remove_group(cx, cy):
    q = deque([(cx, cy)])
    num = maps[cx][cy]
    maps[cx][cy] = -2
    visited = [[False] * n for _ in range(n)]
    visited[cx][cy] = True
    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if maps[nx][ny] == 0:
                    maps[nx][ny] = -2
                    q.append((nx, ny))
                elif maps[nx][ny] == num:
                    maps[nx][ny] = -2
                    q.append((nx, ny))

def gravity():
    for j in range(n):
        for i in range(n-1, -1, -1):
            if maps[i][j] >= 0:
                tmp = i
                for ni in range(i+1, n):
                    if maps[ni][j] != -2:
                        break
                    maps[ni][j] = maps[tmp][j]
                    maps[tmp][j] = -2
                    tmp = ni


def rotate_left():
    new_maps = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_maps[n-1-j][i] = maps[i][j]                        
    return new_maps

while True:
    rst = find_group()
    if rst == None:
        break
    cnt, cx, cy = rst
    ans += cnt ** 2
    remove_group(cx, cy)
    gravity()
    maps = rotate_left()
    gravity()
print(ans, end='')