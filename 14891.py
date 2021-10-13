# 14891 톱니바퀴
import sys
input = sys.stdin.readline

arr = [[] for _ in range(4)]
for i in range(4):
    arr[i] = list(map(int, input().rstrip()))

k = int(input().rstrip())

rotations = []

for i in range(k):
    num, direction = map(int, input().rstrip().split(' '))
    num -= 1
    rotations.append((num, direction))


def calculate(arr):
    total = 0
    for i in range(4):
        if arr[i][0] == 1:
            total += int(2**i)
    return total


for i in range(k):
    num, direction = rotations[i]
    # 시계 방향
    if direction == 1:
        arr[num] = [arr[num][-1]] + arr[num][:-1]
    # 반시계 방향
    else:
        arr[num] = arr[num][1:] + [arr[num][0]]

    # 왼쪽 방향의 톱니와 연쇄적으로 비교
    target = num
    drct = direction
    # 회전하기 전의 톱니 상태에서의 값 구하기
    # 왼쪽 방향으로 확인할 거니까 원래 인덱스가 6인 원소 구해야함

    # 직전에 시계방향으로 회전했으면 현재는 인덱스 7에 가있을 것이고
    if direction == 1:
        value = arr[target][7]
    # 직전에 반시계방향으로 회전했으면 현재는 인덱스 5에 가있을 것임
    else:
        value = arr[target][5]
    while target > 0:
        if value != arr[target - 1][2]:
            # 회전 전에 현재 확인하는 톱니바퀴의 원래 값을 저장 (다음 반복문에서 확인해야 하니까)
            value = arr[target - 1][6]
            # 직전에 회전한 방향이 시계 방향이면 반시계 방향으로 회전
            if drct == 1:
                arr[target - 1] = arr[target - 1][1:] + [arr[target - 1][0]]
                drct = -1
            # 직전에 반시계 방향으로 회전했다면, 시계 방향으로 회전
            else:
                arr[target - 1] = [arr[target - 1][-1]] + arr[target - 1][:-1]
                drct = 1
        else:
            break
        target -= 1

    # 오른쪽 방향의 톱니와 연쇄적으로 비교
    target = num
    drct = direction
    # 회전하기 전의 톱니 상태에서의 값 구하기
    # 오른쪽 방향으로 확인할 거니까 원래 인덱스가 2인 원소 구해야함

    # 직전에 시계방향으로 회전했으면 현재는 인덱스 3에 가있을 것이고
    if direction == 1:
        value = arr[target][3]
    else:
        # 직전에 반시계방향으로 회전했으면 현재는 인덱스 1에 가있을 것임
        value = arr[target][1]
    while target < 3:
        if value != arr[target + 1][6]:
            value = arr[target + 1][2]
            # 직전에 회전한 방향이 시계 방향이면 반시계 방향으로 회전
            if drct == 1:
                arr[target + 1] = arr[target + 1][1:] + [arr[target + 1][0]]
                drct = -1
            # 직전에 반시계 방향으로 회전했다면, 시계 방향으로 회전
            else:
                arr[target + 1] = [arr[target + 1][-1]] + arr[target + 1][:-1]
                drct = 1
        else:
            break
        target += 1

result = calculate(arr)
print(result)
