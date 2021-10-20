# 14499 주사위 굴리기
import sys
input = sys.stdin.readline
from copy import deepcopy

# 세로 n, 가로 m
# 0 <= x <= n - 1
# 0 <= y <= m - 1
n, m, x, y, k = map(int, input().rstrip().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

commands = list(map(int, input().rstrip().split()))
length = len(commands)


# 1  2  3  4  5  6
# 위 뒤 오 왼 앞 아

# 동쪽으로 이동하면 (오른쪽) 
# 4  2  1  6  5  3
# 위 뒤 오 왼 앞 아

# 서쪽으로 이동하면 (왼쪽)
# 3  2  6  1  5  4
# 위 뒤 오 왼 앞 아

# 북쪽으로 이동하면 (위쪽)
# 5  1  3  4  6  2
# 위 뒤 오 왼 앞 아

# 남쪽으로 이동하면 (아래쪽)
# 2  6  3  4  1  5
# 위 뒤 오 왼 앞 아

dice = [0, 0, 0, 0, 0, 0]

# def move(dice, direction):
#     if direction == 0:
        
# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(length):
    command = int(commands[i]) - 1
    # 동 0  서 1  북 2  남 3

    # 주사위 좌표 이동
    nx, ny = x + dx[command], y + dy[command]
    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        continue
    new_dice = deepcopy(dice)
    # 주사위 값도 이동
    # 이동 명령에 따라 주사위 인덱스의 값 변경
    if command == 0:
        # 동
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif command == 1:
        # 서
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif command == 2:
        # 남
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif command == 3:
        # 북
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    dice = new_dice

    # 주사위 바닥 인덱스를 5라고 할때
    # 이동한 칸에 쓰여있는 수가 0이면 주사위의 바닥면에 쓰여있는 수가 칸에 복사됨
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    # 0이 아니면 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되고 칸에 있는 수는 0이 됨
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    print(dice[0])
    x, y = nx, ny
