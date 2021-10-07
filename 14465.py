# 14465 소가 길을 건너간 이유
# 투포인터, 슬라이딩 윈도우
n, k, b = map(int, input().split())
light = [0] * (n + 1)

# 깨진 신호등은 1으로 처리
for _ in range(b):
    light[int(input())] = 1

interval_sum = light
result = int(1e9)

for i in range(1, n+1):
    interval_sum[i] += interval_sum[i-1]

for start in range(k, n+1):
    result = min(result, interval_sum[start] - interval_sum[start - k])

print(result)