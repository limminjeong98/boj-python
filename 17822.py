# 17822 원판 돌리기
import sys
input = sys.stdin.readline
from copy import deepcopy
n, m, t = map(int, input().split())
board = [[0] * (m + 1)]
for i in range(n):
    board.append([0] + list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t):
    x, d, k = map(int, input().split())
    for r in range(1, n + 1):
        if r % x != 0:
            continue
        # 시계 방향
        if d == 0:
            board[r] = [0] + board[r][-k:] + board[r][1:-k]
        # 반시계 방향
        else:
            board[r] = [0] + board[r][k + 1:] + board[r][1:k + 1] 
    total = 0
    for r in range(1, n + 1):
        total += m + 1 - board[r].count(0)
    if total == 0:
        continue
    # tmp_board = deepcopy(board)
    tmp_board = board
    find = False
    for r in range(1, n + 1):
        if board[r].count(0) == m + 1:
            continue
        for c in range(1, m + 1):
            if board[r][c] == 0:
                continue
            flag = False
            for k in range(4):
                nr, nc = r + dx[k], c + dy[k]
                if nr <= 0 or nr > n:
                    continue
                # if nr <= 0:
                #     nr += n
                # elif nr > n:
                #     nr -= n
                if nc <= 0:
                    nc += m
                elif nc > m:
                    nc -= m
                if board[nr][nc] == board[r][c]:
                    tmp_board[nr][nc] = 0
                    flag = True
                    find = True
            if flag:
                tmp_board[r][c] = 0
    if find:
        board = deepcopy(tmp_board)
    else:
        average = 0
        cnt = 0
        for a in range(1, n + 1):
            cnt += m + 1 - board[a].count(0)
            average += sum(board[a])
        average = average / cnt
        for a in range(1, n + 1):
            for b in range(1, m + 1):
                if board[a][b] == 0:
                    continue
                if board[a][b] > average:
                    board[a][b] -= 1
                elif board[a][b] < average:
                    board[a][b] += 1
    # for r in range(1, n + 1):
    #     print(board[r])
    # print()
    
answer = 0
for i in range(1, n + 1):
    answer += sum(board[i])
print(answer)