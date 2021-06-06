from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[None] * 4 for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [tmp[2*j], tmp[2*j+1]-1]
ans = 0

def turn_left(direction):
    return (direction + 1) % 8

def find_fish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i, j)
    return None

def move_fishes(arr, s_x, s_y):
    for i in range(1, 17):
        position = find_fish(arr, i)
        if position != None:
            x, y = position[0], position[1]
            direction = arr[x][y][1]
            for j in range(8):
                nx, ny = x + dx[direction], y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == s_x and ny == s_y):
                        arr[x][y][1] = direction
                        arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                        break
                direction = turn_left(direction)

def get_possible_positions(arr, s_x, s_y):
    positions = []
    direction = arr[s_x][s_y][1]
    for i in range(4):
        s_x += dx[direction]
        s_y += dy[direction]
        if 0 <= s_x < 4 and 0 <= s_y < 4:
            if arr[s_x][s_y][0] != -1:
                positions.append((s_x, s_y))
    return positions

def dfs(arr, x, y, total):
    global ans
    arr = deepcopy(arr)
    total += arr[x][y][0]
    arr[x][y][0] = -1
    move_fishes(arr, x, y)
    positions = get_possible_positions(arr, x, y)
    if len(positions) == 0:
        ans = max(ans, total)
        return
    for position in positions:
        x, y = position
        dfs(arr, x, y, total)

dfs(arr, 0, 0, 0)
print(ans)


