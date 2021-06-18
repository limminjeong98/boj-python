import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

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

for i in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        if a != b:
            union_parent(parent, a, b)
    else:
        if a == b:
            print('YES')
        elif find_parent(parent, a) != find_parent(parent, b):
            print('NO')
        else:
            print('YES')
