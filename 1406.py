# 1406 에디터
import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
m = int(input().rstrip())

stack2 = []

for i in range(m):
    commands = input().rstrip()
    if commands == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif commands == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif commands == 'B':
        if stack1:
            stack1.pop()
    else:
        char = commands[2]
        stack1.append(char)
print(''.join(stack1 + list(reversed(stack2))))