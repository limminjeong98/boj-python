from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, fuel = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = -1

r, c = map(int, input().split())
r -= 1
c -= 1
passengers = []

for _ in range(m):
    start_r, start_c, dest_r, dest_c = map(int, input().split())
    passengers.append((start_r-1, start_c-1, dest_r-1, dest_c-1))

num = len(passengers)
visited = [False] * num
cnt = 0

q = deque(passengers)

def find_next_passenger(x, y):
    next_idx = -1
    next_dist = INF
    for i in range(num):
        if not visited[i]:
            


