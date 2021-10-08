# 1916 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)

# for i in range(n):
#     graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    # graph[a][b] = c
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())


def dijkstra(node):
    h = []
    heapq.heappush(h, (0, node))
    distance[node] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(start)
print(distance[end])
