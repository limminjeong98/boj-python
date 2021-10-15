# 15686 치킨 배달
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
house, chicken = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j)) 
        elif data[j] == 2:
            chicken.append((i, j))

cl = len(chicken)
hl = len(house)

cand = [0] * cl
INF = int(1e9)
answer = INF

# 치킨집을 정한 뒤 각 집부터의 거리를 계산
def cal(cand):
    total = 0
    for hx, hy in house:
        tmp = INF
        for i in range(cl):
            cx, cy = chicken[i]
            if cand[i]:
                tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        total += tmp
    return total

# 치킨 집의 개수가 m개가 될때까지는 계속 추가하고 
# m개가 되면 각 집으로부터 치킨집까지의 최소 거리를 구한다
def dfs(cnt, cand, idx):
    global answer
    if cnt == m:
        result = cal(cand)
        answer = min(answer, result)
    else:
        for i in range(idx, cl):
            if not cand[i]:
                cand[i] = 1
                dfs(cnt + 1, cand, i + 1)
                cand[i] = 0
                
dfs(0, cand, 0)
print(answer)