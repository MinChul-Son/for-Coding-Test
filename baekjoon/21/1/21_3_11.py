# https://www.acmicpc.net/problem/2178
from collections import deque
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
queue = deque()
queue.append([0,0])
move_x = [1, -1, 0, 0]
move_y = [0, 0, -1, 1]
graph[0][0] = 1
while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + move_x[i]
        y = b + move_y[i]
        if 0 <= x < n and 0 <= y < m and graph[x][y] == "1":
            queue.append([x, y])
            graph[x][y] = graph[a][b] + 1
print(graph[n - 1][m - 1])
print(graph)