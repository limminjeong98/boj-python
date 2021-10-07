# 12847 꿀 아르바이트
n, m = map(int, input().split())
t = list(map(int, input().split()))

arr = [0]
interval_sum = 0
end = 0

for start in range(n):
    while end < n and end - start < m:
        interval_sum += t[end]
        end += 1
    arr.append(interval_sum)
    interval_sum -= t[start]

result = max(arr)
print(result)