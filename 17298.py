# 17298 오큰수
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# 원소의 인덱스를 저장하는 스택
stack = []
result = [-1 for _ in range(N)] 
stack.append(0)

i = 1 
while stack and i < N: 
    while stack and arr[stack[-1]] < arr[i]: 
        result[stack[-1]] = arr[i] 
        stack.pop() 
    stack.append(i) 
    i += 1 

print(' '.join(map(str, result)))