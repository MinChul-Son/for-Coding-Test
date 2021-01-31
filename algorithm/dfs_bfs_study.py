# def dfs (graph, v, visited):
#     #현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=" ")
#     #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# from collections import deque

# BFS 메서드 정의
# def bfs(graph, start, visited):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     #큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end=" ")
#         #아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# 각 노드가 연결된 정보를 표현
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# 각 노드가 방문된 정보를 표현
# visited = [False] * 9

# 정의된 DFS 함수 호출
# dfs(graph, 1, visited)

# 정의된 BFS 함수 호출
# bfs(graph, 1, visited)


# # DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
# def dfs(x, y):
#     #주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
#         dfs(x -1, y)
#         dfs(x, y -1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

# #모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         #현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1
# print(result)

