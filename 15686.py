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
rst = INF
def cal(cand):
    tot = 0
    for hx, hy in house:
        tmp = INF
        for i in range(cl):
            cx, cy = chicken[i]
            if cand[i]:
                tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        tot += tmp
    return tot

def sol(cnt, cand, idx):
    global rst
    if cnt == m:
        result = cal(cand)
        rst = min(rst, result)
    else:
        for i in range(idx, cl):
            if not cand[i]:
                cand[i] = 1
                sol(cnt+1, cand, i)
                cand[i] = 0
                
sol(0, cand, 0)
print(rst)