# 17779 게리맨더링 2
n = int(input())
s = [[]]
answer = int(1e9)
for i in range(n):
    s.append([0] + list(map(int, input().split())))

def find(x, y, d1, d2):
    district = [0 for _ in range(6)]
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    # 5번 선거구의 경계선
    for i in range(d1 + 1):
        tmp[x + i][y - i] = 5
        tmp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        tmp[x + i][y + i] = 5
        tmp[x + d1 + i][y - d1 + i] = 5
    # 경계선과 경계선 안에 포함되어 있는 구역도 5번 선거구
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(1, n + 1):
            if tmp[i][j] == 5:
                flag = not flag
            if flag:
                tmp[i][j] = 5
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r < x + d1 and c <= y and tmp[r][c] == 0:
                district[1] += s[r][c]
            elif r <= x + d2 and y < c and tmp[r][c] == 0:
                district[2] += s[r][c]
            elif x + d1 <= r and c < y - d1 + d2 and tmp[r][c] == 0:
                district[3] += s[r][c]
            elif x + d2 < r and y - d1 + d2 <= c and tmp[r][c] == 0:
                district[4] += s[r][c]
            elif tmp[r][c] == 5:
                district[5] += s[r][c]
    return max(district[1:]) - min(district[1:])


for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    answer = min(answer, find(x, y, d1, d2))
print(answer)