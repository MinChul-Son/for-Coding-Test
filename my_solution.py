# import sys
# input = sys.stdin.readline
# N, k  = map(int, input().split())
# max_food = list(map(int, input().split()))

# while True:
#     if max_food[k-1] == 0:
#         print(k, end=" ")
#         max_food[k-1] -= 1
#     elif max_food[k-1] < 0:
#         pass
#     else:
#         max_food[k-1] -= 1
#     if max_food.count(-1) == N:
#         break
#     k += 1
#     if k > N:
#         k %= N

#----------------------------------------------------
import sys
from collections import deque
import copy
input = sys.stdin.readline
N = int(input())
graph = [list(input().strip()) for _ in range(N)]
temp_graph1 = copy.deepcopy(graph)
temp_graph2 = copy.deepcopy(graph)
x1, x2, y1, y2 = map(int, input().split())
total_time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, temp_graph):
    global y1, y2
    if graph[x][y] == 'D':
        return 0
    queue = deque()
    queue.append((x, y))
    temp_graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if temp_graph[nx][ny] == 'X':
                continue
            if temp_graph[nx][ny] == '.':
                temp_graph[nx][ny] = temp_graph[x][y] + 1
                temp_nx = y1 + dx[i]
                temp_ny = y2 + dy[i]
                if temp_nx >= 0 or temp_nx < N or temp_ny >= 0 or temp_ny < N:
                    if temp_graph[temp_nx][temp_ny] == '.':
                        y1 = temp_nx
                        y2 = temp_ny
                queue.append((nx, ny))
            if temp_graph[nx][ny] == 'D':
                return temp_graph[x][y] + 1
    return -1

if bfs(x1, x2, temp_graph1) == -1:
    print(-1)
else:
    total_time += bfs(x1, x2, temp_graph1)
    if bfs(y1, y2, temp_graph2) == -1:
        print(-1)
    else:
        total_time += bfs(y1, y2, temp_graph2)





#---------------------------------------------------
# from itertools import permutations
# import sys
# input = sys.stdin.readline
# N, k = map(int, input().split())