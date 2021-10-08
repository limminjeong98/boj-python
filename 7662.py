# 7662 이중 우선순위 큐
import heapq
import sys
input = sys.stdin.readline

t = int(input().rstrip())
result = []

for _ in range(t):
    minh, maxh = [], []
    visited = [False] * 1000001
    k = int(input().rstrip())
    for index in range(k):
        char, num = input().rstrip().split(' ')
        num = int(num)
        if char == 'I':
            heapq.heappush(maxh, (-num, index))
            heapq.heappush(minh, (num, index))
            visited[index] = True
        else:
            if num == 1:
                while maxh and not visited[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            else:
                while minh and not visited[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)

    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)

    if not maxh:
        # print('EMPTY')
        result.append('EMPTY')
    else:
        # print(-maxh[0][0], minh[0][0])
        result.append(str(-maxh[0][0]) + ' ' + str(minh[0][0]))

print('\n'.join(result))
