# 게으른 백곰
from collections import defaultdict

n, k = map(int, input().split())
ice = defaultdict(int)
left, right = int(1e9), 0
result = 0

for _ in range(n):
    g, x = map(int, input().split())
    ice[x] = g
    left = min(left, x)
    right = max(right, x)

end = left
total = 0

for start in range(left, right + 1):
    while end < right + 1 and end <= start + 2 * k:
        if ice[end] == 0:
            end += 1
            continue
        total += ice[end]
        end += 1
    result = max(result, total)
    total -= ice[start]

print(result)
