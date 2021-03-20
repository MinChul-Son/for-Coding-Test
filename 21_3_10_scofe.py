# import sys
# n = int(sys.stdin.readline())
# times = [list(sys.stdin.readline().split(" ~ ")) for _ in range(n)]
# min_time = times[0][0]
# max_time = times[0][1].strip()
# for i in range(1, n):
#     if min_time < times[i][0]:
#         min_time = times[i][0]
#     if max_time > times[i][1].strip():
#         max_time = times[i][1].strip()
# if min_time > max_time:
#     print(-1)
# else:
#     print(min_time + " ~ " + max_time)
#-------------------------------------------------------------

# import sys
# n = int(sys.stdin.readline())
# load = list(map(int, list(sys.stdin.readline().strip())))
# dp = [0 for _ in range(51)]
# dp[2] = 1
# dp[3] = 2
# dp[4] = 3
# dp[5] = 5
# if n > 5:
#     for i in range(6, n+1):
#         dp[i] = dp[i-1] + (2**(i-4))
# count = 0
# answer = 0
# for i in load:
#     if i == 1:
#         count += 1
#     else:
#         answer += dp[count]
#         count = 0
# answer += dp[count]
# print(answer)


#----------------------------------------------
# import sys
# n = int(sys.stdin.readline())
# graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
# size = [0]
# count = 0
# for i in graph:
#     for j in i:
#         if j == 1:
#             count += 1
# size.append(count)
# for i in range(2, n+1):
#     count = 0
#     for j in range(n-i+1):
#         for k in range(n-i+1):
#             if graph[j][k] == 1:
#                 for p in range(1, i):
#                     if graph[j][k+p] == 1 and graph[j+p][k] == 1 and graph[j+p][k+p] == 1:
#                         continue
#                     break
#                 else:
#                     count += 1              
#     size.append(count)
# print("total: %d" %sum(size))
# for i, p in enumerate(size):
#     if p:
#         print("size[%d]: %d" %(i, p))

#-----------------------------------------------------
# import sys
# grade = list(map(float, sys.stdin.readline().split()))
# grade[0] = (grade[0], 'A')
# grade[1] = (grade[1], 'B')
# grade[2] = (grade[2], 'C')
# grade[3] = (grade[3], 'D')
# grade[4] = (grade[4], 'E')
# n, m = map(int, sys.stdin.readline().split())
# content_state = [list(sys.stdin.readline().strip()) for _ in range(n)]
# content_genre = [list(sys.stdin.readline().strip()) for _ in range(n)]
# recommend = []
# for i in range(n):
#     for j in range(m):
#         if content_state[i][j] == 'Y' or content_state[i][j] == 'O':
#             recommend.append([content_state[i][j], content_genre[i][j],(i,j)])
# for j, p in enumerate(recommend):
#     for i in grade:
#         if i[1] == p[1]:
#             recommend[j].append(i[0])
#             break
# recommend = sorted(recommend, key=lambda x: (-ord(x[0]), -x[3]))
# for i in recommend:
#     print(i[1]+ " " + str(i[3])+ " " + " ".join(list(map(str, i[2]))))



#--------------------------------------------------------------------------
# import sys
# import copy
# from collections import deque
# n, m = map(int, sys.stdin.readline().split())
# display = [list(sys.stdin.readline().strip()) for _ in range(m)]
# dx = [0, 0, 1]
# dy = [1, -1, 0]
# move_l_r = []

# for i,p in enumerate(display[0]):
#     if p == 'c':
#         count = 0
#         graph = copy.deepcopy(display)
#         graph[0][i] = [0,0]
#         queue = deque()
#         queue.append((0, i))
#         while queue:
#             x, y = queue.popleft()
#             for i in range(3):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                     continue
#                 if graph[nx][ny] == '.':
#                     graph[nx][ny] = [graph[x][y][0] + 1 , graph[x][y][1]]
#                     if i != 2:
#                         graph[nx][ny][1] += 1
#                     queue.append((nx, ny))
#         for i in graph[m-1]:
#             if i != 'x' and i != '.':
#                 break
#         else:
#             print(-1)
#             break
#         temp = n * m
#         for i in graph[m-1]:
#             if i == 'x':
#                 pass
#             elif i == '.':
#                 pass
#             else:
#                 if i[1] < temp:
#                     temp = i[1]
#         print(graph)
#         move_l_r.append(temp)
# else:
#     print(min(move_l_r))


#--------------------------------------------------
# import sys
# n, m = map(int, sys.stdin.readline().split())
# pop_up_store = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# # max(dp[i][j-1], dp[i-1][j]) + dp[i][j]
# for i in range(1, n):
#     pop_up_store[0][i] += pop_up_store[0][i-1]
# for i in range(1, m):
#     pop_up_store[i][0] += pop_up_store[i-1][0]
# for i in range(1, m):
#     for j in range(1, n):
#         pop_up_store[i][j] = max(pop_up_store[i][j-1], pop_up_store[i-1][j]) + pop_up_store[i][j]
# print(pop_up_store[-1][-1])