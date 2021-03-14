# https://www.acmicpc.net/problem/7576
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
already_ripen = False
isall_ripen = False
for i in graph:
    if 0 in i:
        break
else:
    already_ripen = True

if already_ripen:
    print(0)
else:
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, -1, 1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + move_x[i]
            y = b + move_y[i]
            if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
                queue.append([x, y])
                graph[x][y] = graph[a][b] + 1
    for i in graph:
        if 0 in i:
            break
    else:
        isall_ripen = True
    if not isall_ripen:
        print(-1)
    else:
        result = 0
        for i in graph:
            for j in i:
                if j > result:
                    result = j
        print(result-1)


