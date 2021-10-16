# 21611 마법사 상어와 블리자드
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))

magic = []
for _ in range(m):
    d, s = map(int, input().rstrip().split())
    magic.append((d - 1, s))

cnt1, cnt2, cnt3 = 0, 0, 0
# 상어의 위치
sx, sy = n // 2, n // 2
# 블리자드 마법 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]

def move_beads(sx, sy):
    global a
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    if a[x][y] != 0:
        beads = [a[x][y]]
    else:
        beads = []
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
    # 방향 d로 거리가 s이하인 모든 칸에 얼음 파편을 던져 구슬을 파괴
    for c in range(s):
        nx, ny = sx + dx[d] * (c + 1), sy + dy[d] * (c + 1)
        if not (0 <= nx < n and 0 <= ny < n):
            break
        a[nx][ny] = 0
    # 구슬이 파괴되어 칸이 비면 이동
    while True:
        move_beads(sx, sy)
        # 더이상 구슬이 이동하지 않을 때까지 반복됨
        flag = delete_beads(sx, sy)
        if flag == 0:
            break
    # 상어 왼쪽 칸부터 구슬이 존재
    x, y = sx, sy - 1
    idx, cnt, move, turn = 0, 0, 1, 1
    flag, tmp = 0, []
    while True:
        # 그룹을 새로 만들어야 하는 경우
        if not flag:
            beads_num, beads_cnt = a[x][y], 1
            flag = 1
        nx, ny = x + dx2[idx], y + dy2[idx]
        # 존재하는 그룹의 구슬 번호와 같은 경우
        if a[nx][ny] == a[x][y]:
            beads_cnt += 1
            # 칸의 크기 끝에 도달하면 그룹도 끝
            if nx == 0 and ny == 0:
                tmp.append(beads_cnt)
                tmp.append(beads_num)
        # 현재까지 그룹만 기록
        else:
            tmp.append(beads_cnt)
            tmp.append(beads_num)
            flag = 0
        x, y = nx, ny
        # 칸의 크기 끝에 도달하면 끝
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