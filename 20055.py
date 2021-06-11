from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([False] * n)
cnt = 0

while True:
    cnt += 1
    a.rotate(1)
    robot.rotate(1)
    robot[n-1] = False
    # 올라가거나 이동할때만 내구도가 감소
    # 내려갈 때는 내구도가 감소하지 않음
    for i in range(n-2, -1, -1):
        if robot[i] == True:
            if not robot[i+1] and a[i+1] > 0:
                robot[i] = False
                robot[i+1] = True
                a[i+1] -= 1
    if robot[n-1]:
        robot[n-1] = False
        
    if not robot[0] and a[0] > 0:
        robot[0] = True
        a[0] -= 1
    if a.count(0) >= k:
        print(cnt)
        break
