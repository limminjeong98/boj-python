
# 1976 여행가자
n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))
flag = True
for i in range(m - 1):
    a, b = plan[i], plan[i + 1]
    if find_parent(parent, a) != find_parent(parent, b):
        print('NO')
        flag = False
        break
if flag:
    print('YES')