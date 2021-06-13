# https://www.acmicpc.net/problem/1303
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
my_power = 0
enemy_power = 0
graph = [list(input().strip()) for _ in range(m)] # 상하좌우만 검사해서 뭉쳐있는 덩어리 제곱
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
team = ''

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    team = graph[x][y]
    count = 1
    graph[x][y] = '.'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == team:
                count += 1
                graph[nx][ny] = '.'
                queue.append((nx, ny))
    return (count, team)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' or graph[i][j] == 'B':
            count,team = bfs(i, j)
            if team == 'W':
                my_power += count**2
            else:
                enemy_power += count **2

print(my_power, enemy_power)

