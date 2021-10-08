# 5430 AC
import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    p = input().rstrip()
    n = int(input().rstrip())
    arr = input().rstrip()
    arr = list(arr[1:-1].split(','))
    q = deque(arr)

    # 뒤집는 횟수가 홀수 번일때만 뒤집기 
    revcnt, front, back = 0, 0, len(q) - 1
    flag = 0
    if n == 0:
        q = []
        front, back = 0, 0

    for i in range(len(p)):
        if p[i] == 'R':
            revcnt += 1
        elif p[i] == 'D':
            if len(q) < 1:
                flag = 1
                print('error')
                break
            else:
                if revcnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == 0:
        if revcnt % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
