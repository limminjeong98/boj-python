# 17144 미세먼지 안녕!
import sys
input = sys.stdin.readline
from copy import deepcopy

r, c, t = map(int, input().rstrip().split())
a = []
ac = []
for i in range(r):
    data = list(map(int, input().rstrip().split()))
    for j in range(c):
        if data[j] == -1:
            ac.append((i, j))
    a.append(data)

# 공기청정기의 값 -1 -> 0으로 바꿔줘야함
for i in range(2):
    x, y = ac[i]
    a[x][y] = 0

# 공기청정기 위칸 기준
dx1 = [0, -1, 0, 1]
dy1 = [1, 0, -1, 0]
# 공기청정기 아래칸 기준
dx2 = [0, 1, 0, -1]
dy2 = [1, 0, -1, 0]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 미세먼지 확산
def diff():
    new_a = deepcopy(a)
    for i in range(r):
        for j in range(c):
            if a[i][j] <= 0:
                continue
            amount = a[i][j] // 5
            cnt = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 > ni or ni >= r or 0 > nj or nj >= c:
                    continue
                if (ni, nj) in ac:
                    continue
                new_a[ni][nj] += amount
                cnt += 1
            new_a[i][j] -= cnt * amount
    return new_a



# 공기청정기 작동
# 각각 한칸씩만 이동!!
def air():
    new_a = deepcopy(a)
    for i in range(2):
        x, y = ac[i]
        rx, ry = x, y
        # 위에 있는 공기청정기
        if i == 0:
            for j in range(4):
                # 가로로 진행할 때 (열이 같은 일직선)
                if j % 2 == 0:
                    col = c - 1
                    while col > 0:
                        nx, ny = x + dx1[j], y + dy1[j]
                        if 0 > nx or nx >= r or 0 > ny or ny >= c:
                            break
                            # col -= 1
                            # continue
                        new_a[nx][ny] = a[x][y]
                        # a[x][y] = 0
                        x, y = nx, ny
                        col -= 1
                # 세로로 진행할 때 (행이 같은 일직선)
                else:
                    row = rx
                    while row > 0:
                        nx, ny = x + dx1[j], y + dy1[j]
                        if 0 > nx or nx >= r or 0 > ny or ny >= c:
                            break
                            # row -= 1
                            # continue
                        new_a[nx][ny] = a[x][y]
                        # a[x][y] = 0
                        x, y = nx, ny
                        row -= 1
            new_a[rx][ry] = 0
        else:
            for j in range(4):
                 # 가로로 진행할 때
                if j % 2 == 0:
                    col = c - 1
                    while col > 0:
                        nx, ny = x + dx2[j], y + dy2[j]
                        if 0 > nx or nx >= r or 0 > ny or ny >= c:
                            break
                            # col -= 1
                            # continue
                        # a[nx][ny] += a[x][y]
                        new_a[nx][ny] = a[x][y]
                        # a[x][y] = 0
                        x, y = nx, ny
                        col -= 1
                else:
                    row = r - rx - 1
                    while row > 0:
                        nx, ny = x + dx2[j], y + dy2[j]
                        if 0 > nx or nx >= r or 0 > ny or ny >= c:
                            break
                            # row -= 1
                            # continue
                        # a[nx][ny] += a[x][y]
                        new_a[nx][ny] = a[x][y]
                        # a[x][y] = 0
                        x, y = nx, ny
                        row -= 1
            new_a[rx][ry] = 0
    return new_a



while t > 0:
    a = diff()
    a = air()
    t -= 1

answer = 0
for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            answer += a[i][j]
print(answer)