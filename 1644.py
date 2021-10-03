import math
n = int(input())
prime_numbers = []
arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        prime_numbers.append(i)

cnt = 0
interval_sum = 0
end = 0

for start in range(len(prime_numbers)):
    while interval_sum < n and end < len(prime_numbers):
        interval_sum += prime_numbers[end]
        end += 1

    if interval_sum == n:
        cnt += 1
    interval_sum -= prime_numbers[start]

print(cnt)