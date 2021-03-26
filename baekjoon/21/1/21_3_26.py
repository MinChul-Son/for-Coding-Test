# https://www.acmicpc.net/problem/10026
import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, color):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if visited[x][y] == 0:
        if graph[x][y] == color:
            # 해당 노드 방문 처리
            visited[x][y] = 1
            # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
            dfs(x -1, y, color)
            dfs(x, y -1, color)
            dfs(x + 1, y, color)
            dfs(x, y + 1, color)
            return True
    return False

n= int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = 0
# 일반 사람 DFS
for i in range(n):
    for j in range(n):
        #현재 위치에서 DFS 수행
        if dfs(i,j,graph[i][j]) == True:
            result += 1
print(result, end=" ")
# 적록색약 DFS
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[0] * n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        #현재 위치에서 DFS 수행
        if dfs(i,j,graph[i][j]) == True:
            result += 1
print(result, end=" ")