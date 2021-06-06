import sys
input = sys.stdin.readline
n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
tx, ty = n//2, n//2
result = 0
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
#          2% 
#     10%  7%  1%
#  5%  a   y <- x
#     10%  7%  1%
#          2%
#       4
#    2  5  8
# 1
#    3  6  9
#       7
torX = [(0, -1, 1, -2, -1, 1, 2, -1, 1),
        (2, 1, 1, 0, 0, 0, 0, -1, -1),
        (0, 1, -1, 2, 1, -1, -2, 1, -1),
        (-2, -1, -1, 0, 0, 0, 0, 1, 1)]
torY = [(-2, -1, -1, 0, 0, 0, 0, 1, 1),
        (0, -1, 1, -2, -1, 1, 2, -1, 1),
        (2, 1, 1, 0, 0, 0, 0, -1, -1),
        (0, 1, -1, 2, 1, -1, -2, 1, -1)]
sand = (0.05, 0.1, 0.1, 0.02, 0.07, 0.07, 0.02, 0.01, 0.01)

drct = 0 # direction
dst = 1 # distance
flag = False

while True:
    for i in range(dst):
        nx, ny = tx + dx[drct], ty + dy[drct]
        sumSand = 0
        for d in range(9):
            nx2, ny2 = nx + torX[drct][d], ny + torY[drct][d]
            tmpSand = int(maps[nx][ny] * sand[d])
            sumSand += tmpSand
            if 0 <= nx2 < n and 0 <= ny2 < n:
                maps[nx2][ny2] += tmpSand
            else:    
                result += tmpSand
        maps[nx][ny] -= sumSand
        nx3, ny3 = nx + dx[drct], ny + dy[drct]
        if 0 <= nx3 < n and 0 <= ny3 < n:
            maps[nx3][ny3] += maps[nx][ny]
        else:
            result += maps[nx][ny]
        maps[nx][ny] = 0
        tx, ty = nx, ny
        if tx == 0 and ty == 0:
            flag = True
            break
    if flag:
        break
    if drct == 1 or drct == 3:
        dst += 1
    drct = (drct + 1) % 4
        
print(result)          