# 17281 야구
n = int(input())
rst = []
for _ in range(n):
    rst.append(list(map(int, input().split())))
select, visited = [0 for _ in range(9)], [0 for _ in range(9)]
select[3], visited[3] = 0, 1
ans = 0

def dfs(cnt):
    global ans
    if cnt == 9:
        idx, score = 0, 0
        for inning in rst:
            out, base1, base2, base3 = 0, 0, 0, 0
            while out < 3:
                cur = select[idx]
                if inning[cur] == 0:
                    out += 1
                elif inning[cur] == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif inning[cur] == 2:
                    score += base3 + base2
                    base1, base2, base3 = 0, 1, base1
                elif inning[cur] == 3:
                    score += base3 + base2 + base1
                    base1, base2, base3 = 0, 0, 1
                else:
                    score += base3 + base2 + base1 + 1
                    base1, base2, base3 = 0, 0, 0
                idx += 1
                if idx >= 9:
                    idx -= 9
        ans = max(ans, score)
        return
    
    for i in range(9):
        if visited[i]:
            continue
        visited[i] = 1
        select[i] = cnt
        dfs(cnt + 1)
        visited[i] = 0
        select[i] = 0
        
dfs(1)
print(ans)