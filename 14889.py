# 14889 스타트와 링크
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
result = int(1e9)

for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

select = [False] * n


def dfs(idx, cnt):
    global result
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += arr[i][j]
                elif not select[i] and not select[j]:
                    link += arr[i][j]
        result = min(result, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = True
        dfs(i + 1, cnt + 1)
        select[i] = False


dfs(0, 0)
print(result)
