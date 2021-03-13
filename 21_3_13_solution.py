# def dfs(x, y, n, m, graph):
#     global find_key, find_box
#     find_key = False
#     find_box = False
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 2:
#         find_box = True
#         temp1 = True
#     if graph[x][y] == 4:
#         find_key = True
#         temp2 = True
#     if graph[x][y] == 0 or graph[x][y] == 3:
#         graph[x][y] = -1
#         dfs(x-1, y, n, m, graph)
#         dfs(x+1, y, n, m, graph)
#         dfs(x, y-1, n, m, graph)
#         dfs(x, y+1, n, m, graph)

# def main():
#     t = int(input())
#     global temp1, temp2
#     temp1 = False
#     temp2 = False
#     for _ in range(t):
#         n, m =map(int, input().split())
#         find_key = False
#         find_box = False
#         graph = [list(map(int, input().split())) for _ in range(n)]
#         #소마 위치 찾기
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] == 3:
#                     dfs(i, j, n, m, graph)
#         if temp1 and temp2:
#             print(1)
#         else:
#             print(0)
# if __name__=="__main__":
#     main()
from collections import deque
def main():
    t = int(input())
    for _ in range(t):
        n, m =map(int, input().split())
        graph = [list(map(int, input().split())) for _ in range(n)]
        find_soma = False
        find_box = False
        find_key = False
        queue = deque()
        queue.append([0, 0])
        move_x = [1, -1, 0, 0]
        move_y = [0, 0, -1, 1]
        graph[0][0] = -1

        while queue:
            a, b = queue.popleft()
            for i in range(4):
                x = a + move_x[i]
                y = b + move_y[i]
                if 0 <= x < n and 0 <= y < m and (graph[x][y] == 0 or graph[x][y] == 2 or graph[x][y] == 3 or graph[x][y] == 4):
                    queue.append([x, y])
                    if graph[x][y] == 2:
                        find_box = True
                    elif graph[x][y] == 3:
                        find_soma = True
                    elif graph[x][y] == 4:
                        find_key = True
                    graph[x][y] = -1
        if find_box and find_key and find_soma:
            print(1)
        else:
            print(0)
if __name__=="__main__":
    main()


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