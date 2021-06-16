import sys
input = sys.stdin.readline
n = int(input())
step = []
for i in range(n):
    step.append(int(input()))
dp = []
# 계단의 갯수가 1개,2개일 때를 생각해서 
dp.append(step[0])
if n > 2:
    dp.append(max(step[0] + step[1], step[1]))
    dp.append(max(step[0] + step[2], step[1]+step[2]))
    for k in range(3, n):
        dp.append(max(dp[k-2]+step[k], dp[k-3]+step[k-1]+step[k]))
    print(dp.pop())
elif n == 1:
    print(step[0])
else:
    print(step[0]+step[1])