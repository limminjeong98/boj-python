# 15685 드래곤커브
# 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 0 <= x <= 100, 0 <= y <= 100 
a = [[0] * 101 for _ in range(101)]

n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    dragon = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(dragon)):
            # k세대 드래곤 커브는 k-1세대 드래곤 커브를 
            # 끝점을 기준으로 90도 시계방향 회전시킨
            # 다음 끝점에 붙인것
            tmp.append((dragon[-i - 1] + 1) % 4)
        dragon.extend(tmp)
    for i in dragon:
        nx, ny = x + dx[i], y + dy[i]
        a[nx][ny] = 1
        x, y = nx, ny

answer = 0
for i in range(100):
    for j in range(100):
        if a[i][j] != 1:
            continue
        # 정사각형 네 꼭지점이 모두 드래곤 커브의 일부인지 확인
        if a[i + 1][j] and a[i][j + 1] and a[i + 1][j + 1]:
            answer += 1
print(answer)
