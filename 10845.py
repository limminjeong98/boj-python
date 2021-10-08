import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    commands = input().rstrip()

    if commands == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif commands == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif commands == 'size':
        print(len(q))
    elif commands == 'front':
        if not q:
            print(-1)
        else:
            print(q[0]) 
    elif commands == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
    else:
        com, num = commands.split(' ')
        q.append(int(num))