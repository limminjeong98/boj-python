# 2493 탑
n = int(input())
top = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    while stack:
        # 더 높은 탑이 왼쪽(stack)에 있어서 수신 가능한 상황
        if stack[-1][1] > top[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    # stack이 비면 레이저를 수신할 탑이 없다.
    if not stack:
        answer.append(0)
    stack.append((i, top[i])) # 인덱스, 값

print(' '.join(map(str, answer)))