
# 20055 컨베이어 벨트 위의 로봇
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
a = deque(map(int, input().rstrip().split()))
robot = deque([False] * n)
cnt = 0

while True:
    cnt += 1
    a.rotate(1)
    robot.rotate(1)
    # 내리는 위치에 도달하면 즉시 내린다
    robot[n - 1] = False
    # 올라가거나 이동할때만 내구도가 감소
    # 내려갈 때는 내구도가 감소하지 않음
    for i in range(n - 2, -1, -1):
        if robot[i] == True:
            # 칸에 로봇이 없고 내구도가 0보다 커야 함
            if not robot[i + 1] and a[i + 1] > 0:
                robot[i] = False
                robot[i + 1] = True
                a[i + 1] -= 1
    # 언제든지 로봇이 내리는 위치에 도달하면 내린다
    # n - 2에서 n - 1로 왔으면 즉시 내린다
    if robot[n - 1]:
        robot[n - 1] = False
        
    if not robot[0] and a[0] > 0:
        robot[0] = True
        a[0] -= 1
    # 내구도가 0인 칸의 개수가 k개 이상이라면 종료
    if a.count(0) >= k:
        print(cnt)
        break
