import heapq
v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (v+1)
maps = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))

q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
        continue
    for i in maps[node]:
        if distance[i[0]] > dist + i[1]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(q, (distance[i[0]], i[0]))

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
