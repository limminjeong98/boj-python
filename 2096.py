# 2096 내려가기
# 메모리 제한 때문에 dp로 해결 X
import sys
input = sys.stdin.readline

n = int(input())

# 3 * n 크기가 아니라 3 * 2 크기로 설정
# 이전과 현재에 대한 값만 저장하는 배열
max_arr = [[0] * 3 for _ in range(2)]
min_arr = [[0] * 3 for _ in range(2)]

for i in range(n):
    tmp = list(map(int, input().split()))

    max_arr[1][0] = max(max_arr[0][0], max_arr[0][1]) + tmp[0]
    min_arr[1][0] = min(min_arr[0][0], min_arr[0][1]) + tmp[0]

    max_arr[1][1] = max(max_arr[0][0], max_arr[0][1], max_arr[0][2]) + tmp[1]
    min_arr[1][1] = min(min_arr[0][0], min_arr[0][1], min_arr[0][2]) + tmp[1]

    max_arr[1][2] = max(max_arr[0][1], max_arr[0][2]) + tmp[2]
    min_arr[1][2] = min(min_arr[0][1], min_arr[0][2]) + tmp[2]

    max_arr[0][0], max_arr[0][1], max_arr[0][2] = max_arr[1][0], max_arr[1][1], max_arr[1][2]
    min_arr[0][0], min_arr[0][1], min_arr[0][2] = min_arr[1][0], min_arr[1][1], min_arr[1][2]

print(max(max_arr[1]), min(min_arr[1]))