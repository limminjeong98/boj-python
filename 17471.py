from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
ans = INF
n = int(input())
people = list(map(int, input().split()))
a = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1, x[0]+1):
        a[i].append(x[j]-1)

def bfs(g):
    q = deque()
    check = [0 for _ in range(n)]
    q.append(g[0])
    check[g[0]] = 1
    cnt, total = 1, 0
    while q:
        x = q.popleft()
        total += people[x]
        for nx in a[x]:
            if nx in g and not check[nx]:
                check[nx] = 1
                cnt += 1
                q.append(nx)
    if cnt == len(g):
        return total
    return 0

def dfs(cnt, x, target):
    global ans
    if cnt == target:
        g1, g2 = deque(), deque()
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1)
        if not ans1:
            return
        ans2 = bfs(g2)
        if not ans2:
            return
        ans = min(ans, abs(ans1-ans2))
        return

    for i in range(x, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(cnt+1, i, target)
        visited[i] = 0

for i in range(1, n//2 + 1):
    visited = [0 for _ in range(n)]
    dfs(0, 0, i)

if ans == INF:
    print(-1)
else:
    print(ans)
