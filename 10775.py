# 10775 공항
import sys
input = sys.stdin.readline

g = int(input().rstrip())
p = int(input().rstrip())

result = 0

parents = [i for i in range(g + 1)]

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if b > a:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(p):
    plane = find_parent(parents, int(input().rstrip()))
    if plane != 0:
        union_parent(parents, plane, plane - 1)
        result += 1
    else:
        break

print(result)