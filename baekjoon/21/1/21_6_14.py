# https://www.acmicpc.net/problem/1743
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [['.' for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = '#'
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    graph[x][y] = 'c'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                count += 1
                graph[nx][ny] = 'c'
                queue.append((nx, ny))
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            count = max(count, bfs(i,j))
print(count)