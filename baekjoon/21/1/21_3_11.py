# https://www.acmicpc.net/problem/2178
# from collections import deque
# n, m = map(int, input().split())
# graph = [list(input()) for _ in range(n)]
# queue = deque()
# queue.append([0,0])
# move_x = [1, -1, 0, 0]
# move_y = [0, 0, -1, 1]
# graph[0][0] = 1
# while queue:
#     a, b = queue.popleft()
#     for i in range(4):
#         x = a + move_x[i]
#         y = b + move_y[i]
#         if 0 <= x < n and 0 <= y < m and graph[x][y] == "1":
#             queue.append([x, y])
#             graph[x][y] = graph[a][b] + 1
# print(graph[n - 1][m - 1])


# https://www.acmicpc.net/problem/2667
# def dfs(x, y):
#     global count
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#     if graph[x][y] == '1':
#         count += 1
#         graph[x][y] = 2       
#         dfs(x -1, y)
#         dfs(x, y -1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False

# n = int(input())
# graph = [list(input()) for _ in range(n)]
# result = 0
# count = 0
# count_list = []
# for i in range(n):
#     for j in range(n):
#         if dfs(i,j) == True:
#             result += 1
#             count_list.append(count)
#             count = 0
# print(result)
# for i in sorted(count_list):
#     print(i)


# answer = 0
# for i in range(1,11):
#     answer += i
# print(answer)