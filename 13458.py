n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for i in range(n):
    if arr[i] <= b:
        answer += 1
        continue
    answer += 1
    if (arr[i] - b) % c != 0:
        answer += 1
    answer += (arr[i] - b) // c
print(answer)