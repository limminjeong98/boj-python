# import sys
INF = int(1e9)
# input = sys.stdin.readline
tc = int(input().rstrip())
for t in range(tc):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    cumsum = {-1:0}
    for i in range(len(arr)):
        cumsum[i] = cumsum[i-1] + arr[i]

    dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

    for gap in range(1, len(arr)):
        for start in range(len(arr)):
            end = start + gap
            if end == len(arr):
                break
            dp[start][end] = INF
            for i in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][i] + dp[i+1][end] + cumsum[end] - cumsum[start-1])

    print(dp[0][-1])
