# 14500 테트로미노
# 8:11 - 8:46
import sys
input = sys.stdin.readline

# 세로n 가로m
n, m = map(int, input().rstrip().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = 0

squares = [((0, 0), (0, 1), (0, 2), (0, 3)),
           ((0, 0), (0, 1), (1, 0), (1, 1)),
           ((0, 0), (1, 0), (2, 0), (2, 1)),
           ((0, 0), (1, 0), (1, 1), (2, 1)),
           ((0, 0), (0, 1), (0, 2), (1, 1))
           ]

# (2, 1)
# 0 0 0 0
# 0 0 0 0
# 0 1 0 0
# 0 0 0 0

# (1, 1)
# 0 0 0 0
# 0 1 0 0
# 0 0 0 0
# 0 0 0 0

# 맵을 회전하는 함수
def rotate(arr):
    # 오른쪽 방향으로 90도 회전
    # (i, j) => ()
    n, m = len(arr), len(arr[0])
    result = [[-1] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = arr[i][j]
    return result


# 맵을 대칭하는 함수
def mirror(arr, idx):
    # 대칭하지 않는 원본
    if idx == 0:
        return arr
    n, m = len(arr), len(arr[0])
    result = [[-1] * m for _ in range(n)]
    # 위(아래)로 대칭
    if idx == 1:
        for i in range(n):
            for j in range(m):
                result[n - 1 - i][j] = arr[i][j]
    # 왼쪽(오른쪽)으로 대칭
    elif idx == 2:
        for i in range(n):
            for j in range(m):
                result[i][m - 1 - j] = arr[i][j]
    return result


# 맺 자체를 대칭시켜서 확인
for r in range(3):
    arr = mirror(arr, r)
    # 맵 자체를 회전시켜서 확인
    for i in range(4):
        arr = rotate(arr)
        n, m = len(arr), len(arr[0])
        for x in range(n):
            for y in range(m):
                # 5개의 테트로미노에 대해서 가장 작은 각 정사각형을 확인해서
                # 가능한 경우일 경우는 값을 체크
                for j in range(5):
                    possible = True
                    square = squares[j]
                    tmp = 0
                    size = len(square)
                    for s in range(size):
                        nx = x + square[s][0]
                        ny = y + square[s][1]
                        if 0 > nx or nx >= n or 0 > ny or ny >= m:
                            possible = False
                            break
                        tmp += arr[nx][ny]
                    if possible:
                        result = max(result, tmp)

# 맵 자체를 대칭시켜서 확인
# 대칭은 두번만 하면 됨
# 위로 대칭한 결과는 아래로 대칭한 결과와 같음
# 왼쪽으로 대칭한 결과는 오른쪽으로 대칭한 결과와 같음
# 즉 총 3개의 맵이 생기게 됨
# 대칭 * 회전을 고려하여야 하므로
print(result)
