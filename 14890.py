# 14890 경사로
# 한 행 또는 열 처음부터 끝까지를 지나갈 수 있으면 길
# 길을 지나갈 수 있으려면 모든 칸의 높이가 같아야 한다
# 경사로를 놓을 수 있고, 길이 L
# 경사로는 낮은 칸에서 높은 칸으로 놓게 되며
# L개의 연속한 칸에 경사로의 바닥이 모두 접해야 한다
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야하고
# L개의 칸이 연속되어 있어야 한다
from copy import deepcopy
n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

def check(arr):
    # 경사로를 놓았는지 체크
    visited = [False for _ in range(n)]
    # 배열의 총 칸이 n개니까 n - 1번 확인함
    for i in range(n - 1):
        # 칸의 높이가 같다면 패스
        if arr[i] == arr[i + 1]:
            continue
        # 높이가 2이상 차이가 난다면 불가능
        if abs(arr[i] - arr[i + 1]) > 1:
            return False
        # 높은 칸 -> 낮은 칸
        if arr[i] > arr[i + 1]:
            # 경사로를 시작, 경사로의 높이를 저장
            height = arr[i + 1]
            # 경사로의 길이는 정확히 L
            for j in range(i + 1, i + l + 1):
                if 0 <= j < n:
                    # 높이가 다르다면 불가능
                    if arr[j] != height:
                        return False
                    # 이미 경사로를 놓은 지점이라면 불가능
                    if visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        # 낮은 칸 -> 높은 칸
        else:
            height = arr[i]
            # i + 1 칸이 높은 칸이었으므로
            # i 부터 거꾸로 i - l + 1 까지 경사로를 놓음
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if arr[j] != height:
                        return False
                    if visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

cnt = 0
# 같은 행들로 카운트
for i in s:
    if check(i):
        cnt += 1
# 같은 열들로 카운트
tmp = deepcopy(s)
for i in range(n):
    for j in range(n):
        tmp[j][n - 1 - i] = s[i][j]
s = tmp
for i in s:
    if check(i):
        cnt += 1
print(cnt)