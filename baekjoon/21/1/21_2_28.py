# https://www.acmicpc.net/problem/1260
# from collections import deque
# def bfs(edge_list,visited, start):
#     queue = deque([start])
#     visited[start] = False
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in range(1, n+1):
#             if visited[i] and edge_list[v][i]:
#                 queue.append(i)
#                 visited[i] = False

# def dfs(edge_list,visited, start):
#     visited[start] = True
#     print(start, end=" ")
#     for i in range(1, n+1):
#         if not visited[i] and edge_list[start][i]:
#             dfs(edge_list, visited, i)

# n, m, v = map(int, input().split())

# edge_list = [[0]* (n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     edge_list[a][b] = 1
#     edge_list[b][a] = 1
# visited = [False for _ in range(n+1)]
# dfs(edge_list, visited, v)
# print()
# bfs(edge_list, visited, v)


# https://www.acmicpc.net/problem/2606
# from collections import deque
# n = int(input())
# m = int(input())
# graph = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
# visited = [False for _ in range(n+1)]
# count = 0
# queue = deque([1])
# visited[1] = True
# while queue:
#     v = queue.popleft()
#     for i in range(1, n+1):
#         if not visited[i] and graph[v][i]:
#             queue.append(i)
#             visited[i] = True
#             count += 1
# print(count)


# https://www.acmicpc.net/problem/2178
