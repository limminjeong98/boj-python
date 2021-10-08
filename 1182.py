# 1182 부분수열의 합
from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

cnt = 0


def dfs(idx, total):
    global cnt
    if idx >= n:
        return
    if total == s:
        cnt += 1
    for i in range(idx + 1, n):
        # total += arr[i]
        dfs(i, total + arr[i])
        # total -= arr[i]


for i in range(n):
    dfs(i, arr[i])
print(cnt)
