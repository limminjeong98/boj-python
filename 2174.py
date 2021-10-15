# 2174 로봇 시뮬레이션
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())
maps = [[-1] * a for _ in range(b)]

# 가로 = 0 ~ a - 1 => x 좌표 (일반적인 y)
# 세로 = 0 ~ b - 1 => y 좌표 (일반적인 x)
robots = []
for i in range(n):
    x, y, d = input().rstrip().split()
    x = int(x) - 1
    y = int(y) - 1
    robots.append((y, x, d))
    maps[y][x] = i


#   N
# W   E
#   S
# N W S E
# L 왼쪽으로 90도 회전
# R 오른쪽으로 90도 회전
# F 앞으로 한 칸 전진
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def rotate(direction, y, x, command):
    if direction == 'N':
        idx = 0
    elif direction == 'W':
        idx = 1
    elif direction == 'S':
        idx = 2
    else:
        idx = 3

    if command == 'F':
        nx, ny = x + dx[idx], y + dy[idx]
        return direction, ny, nx
    else:
        if command == 'L':
            idx += 1
            if idx > 3:
                idx = 0
        elif command == 'R':
            idx -= 1
            if idx < 0:
                idx = 3
        if idx == 0:
            direction = 'N'
        elif idx == 1:
            direction = 'W'
        elif idx == 2:
            direction = 'S'
        else:
            direction = 'E'
        return direction, y, x


commands = []
for i in range(m):
    robot, command, repeat = input().rstrip().split()
    robot = int(robot) - 1
    repeat = int(repeat)
    commands.append((robot, command, repeat))

collision = False
err = ''
for i in range(m):
    if collision:
        break
    robot, command, repeat = commands[i]
    while repeat > 0:
        if collision:
            break
        y, x, direction = robots[robot]
        maps[y][x] = -1
        direction, y, x = rotate(direction, y, x, command)
        # 로봇이 땅의 범위를 벗어나 벽에 충돌하는 경우
        if x < 0 or x >= a or y < 0 or y >= b:
            collision = True
            err = f'Robot {robot + 1} crashes into the wall'
            break
        # 로봇이 움직이다가 다른 로봇에 충돌하는 경우
        # 맵에 로봇번호가 있는지 확인
        elif maps[y][x] != -1:
            collision = True
            err = f'Robot {robot + 1} crashes into robot {maps[y][x] + 1}'
            break
        maps[y][x] = robot
        # 로봇 번호별로 현재 위치와 방향을 로봇 리스트의 로봇 번호에 해당하는 인덱스에 다시 저장해야 함
        robots[robot] = (y, x, direction)
        repeat -= 1


if collision:
    print(err)
else:
    print('OK')
