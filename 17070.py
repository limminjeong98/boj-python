n = int(input())
maps = [[] for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
# dp[0]은 가로, dp[1]은 세로, dp[2]는 대각선

for i in range(n):
    maps[i] = list(map(int, input().split()))
    
dp[0][0][1] = 1

# dp 테이블의 첫 행의 모든 열들을 초기화
for i in range(2, n):
    if maps[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, n):
    for c in range(1, n):
        if maps[r][c] == 0 and maps[r][c-1] == 0 and maps[r-1][c] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
        if maps[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
            
print(sum(dp[i][n-1][n-1] for i in range(3)))