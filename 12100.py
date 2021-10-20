# 12100. 2048 (Easy)
from copy import deepcopy

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

def move(direction):
    global arr
    # 상
    if direction == 0:
        for j in range(n):
            # 맨 위칸부터 차례대로 아래칸까지 비교한다.
            idx = 0
            for i in range(1, n):
                # 비교할 아래칸이 0이면 다음칸과 비교한다.
                # 이때 arr[idx][j]와 다음칸을 비교하기 위해 idx는 변경하지 않는다.
                if arr[i][j] == 0:
                    continue
                # 일단 현재 비교되는 아래칸을 0이라 처리
                tmp = arr[i][j]
                arr[i][j] = 0
                # 비교대상인 위칸이 0이라면 아래칸에서 위칸으로 그대로 올라갈 수 있다.
                if arr[idx][j] == 0:
                    arr[idx][j] = tmp
                # 비교대상인 위칸이 아래칸의 값과 같다면 위칸에 2배를 곱한다.
                # 한번 처리된 칸은 이번 회전에서는 더이상 처리되지 못하므로 idx를 증가시킨다.
                elif arr[idx][j] == tmp:
                    arr[idx][j] = tmp * 2
                    idx += 1
                # 위칸과 아래칸이 같지 않고 둘다 0이 아니라면
                # 비교할 idx를 증가시키고 원래 idx + 1인 칸에 값을 저장한다.
                # 왜냐하면 idx랑 i 사이에 칸이 있다면 이 칸은 무조건 0일 것이라서
                # ㅁ 현재 idx == 0
                # ㅁ
                # ㅁ i == 2 만약 [idx][j] != [i][j] 이고 [i][j] != 0이라면
                # ㅁ i == 1에서 1증가한 상태이므로 [1][j]는 비어있는 상태임 (continue해서 내려왔으니까)
                # ㅁ
                else:
                    idx += 1
                    arr[idx][j] = tmp
    # 하
    elif direction == 1:
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if arr[i][j] == 0:
                    continue
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[idx][j] == 0:
                    arr[idx][j] = tmp
                elif arr[idx][j] == tmp:
                    arr[idx][j] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    arr[idx][j] = tmp
    # 좌
    elif direction == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if arr[i][j] == 0:
                    continue
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][idx] == 0:
                    arr[i][idx] = tmp
                elif arr[i][idx] == tmp:
                    arr[i][idx] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    arr[i][idx] = tmp
    # 우
    else:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if arr[i][j] == 0:
                    continue
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][idx] == 0:
                    arr[i][idx] = tmp
                    arr[i][j] = 0
                elif arr[i][idx] == tmp:
                    arr[i][idx] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    arr[i][idx] = tmp


def dfs(cnt):
    global answer, arr
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > answer:
                    answer = arr[i][j]
        return
    # 현재 cnt 기준으로 최신 arr을 저장해둠
    tmp_arr = deepcopy(arr)
    # 상하좌우 네 방향
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        # 리스트는 deepcopy로 복사하기
        arr = deepcopy(tmp_arr)

dfs(0)
print(answer)