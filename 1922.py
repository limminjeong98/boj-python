# 1922 네트워크 연결
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)

parents = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append((c, a, b))


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


total = 0
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        total += cost

print(total)
