from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
magic = []
for _ in range(m):
    d, s = map(int, input().split())
    magic.append((d-1, s))

cnt1, cnt2, cnt3 = 0, 0, 0
sx, sy = n // 2, n // 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]

def move_beads(sx, sy):
    global a
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    beads = [a[x][y]] if a[x][y] != 0 else []
    while True:
        nx, ny = x + dx2[idx], y + dy2[idx]
        if a[nx][ny] != 0:
            beads.append(a[nx][ny])
        x, y = nx, ny
        if x == 0 and y == 0:
            break
        idx, cnt, move, turn = change_direction(idx, cnt, move, turn)

    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    a = [[0] * n for _ in range(n)]
    if beads:
        a[x][y] = beads[0]
        for bead in beads[1:]:
            nx, ny = x + dx2[idx], y + dy2[idx]
            a[nx][ny] = bead
            x, y = nx, ny
            idx, cnt, move, turn = change_direction(idx, cnt, move, turn)


def delete_beads(sx, sy):
    global cnt1, cnt2, cnt3
    x, y = sx, sy - 1
    idx, cnt, move, turn, flag = 0, 0, 1, 1, 0
    q = []
    while True:
        if not q:
            q.append((x, y))
        nx, ny = x + dx2[idx], y + dy2[idx]
        if a[nx][ny] == a[x][y]:
            q.append((nx, ny))
            if nx == 0 and ny == 0:
                if len(q) >= 4:
                    flag = 1
                    for i, j in q:
                        if a[i][j] == 1:
                            cnt1 += 1
                        elif a[i][j] == 2:
                            cnt2 += 1
                        elif a[i][j] == 3:
                            cnt3 += 1
                        a[i][j] = 0
        else:
            if len(q) >= 4:
                flag = 1
                for i, j in q:
                    if a[i][j] == 1:
                        cnt1 += 1
                    elif a[i][j] == 2:
                        cnt2 += 1
                    elif a[i][j] == 3:
                        cnt3 += 1
                    a[i][j] = 0
            q = []
        x, y = nx, ny

        if (x == 0 and y == 0) or a[x][y] == 0:
            return flag

        idx, cnt, move, turn = change_direction(idx, cnt, move, turn)

def change_direction(idx, cnt, move, turn):
    cnt += 1
    if cnt == turn:
        idx = (idx + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            turn += 1
            move = 0

    return idx, cnt, move, turn

for i in range(m):
    d, s = magic[i]
    for c in range(s):
        nx, ny = sx + dx[d] * (c+1), sy + dy[d] * (c+1)
        if not (0 <= nx < n and 0 <= ny < n):
            break
        a[nx][ny] = 0
    
    while True:
        move_beads(sx, sy)
        flag = delete_beads(sx, sy)
        if flag == 0:
            break
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    flag, tmp = 0, []
    while True:
        if not flag:
            beads_num, beads_cnt = a[x][y], 1
            flag = 1
        nx, ny = x + dx2[idx], y + dy2[idx]
        if a[nx][ny] == a[x][y]:
            beads_cnt += 1
            if nx == 0 and ny == 0:
                tmp.append(beads_cnt)
                tmp.append(beads_num)
        else:
            tmp.append(beads_cnt)
            tmp.append(beads_num)
            flag = 0
    
        x, y = nx, ny
        if (x == 0 and y == 0) or a[x][y] == 0:
            break
        idx, cnt, move, turn = change_direction(idx, cnt, move, turn)
    
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    a = [[0] * n for _ in range(n)]
    if tmp:
        a[x][y] = tmp[0]
        for k in tmp[1:]:
            nx, ny = x + dx2[idx], y + dy2[idx]
            a[nx][ny] = k
            x, y = nx, ny
            if x == 0 and y == 0:
                break
            idx, cnt, move, turn = change_direction(idx, cnt, move, turn)
    
print(cnt1 + 2 * cnt2 + 3 * cnt3)



