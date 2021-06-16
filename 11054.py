n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
r_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
arr.reverse()

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)

rst = 0
for i in range(n):
    rst = max(rst, dp[i]+r_dp[n-1-i]-1)
print(rst)