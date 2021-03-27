# n, my_time = input().split()
# n = int(n)
# my_time = list(my_time.split(':'))
# my_time = 60*60*int(my_time[0]) + 60*int(my_time[1]) + int(my_time[2])
# play_list = [list(input().split(':')) for _ in range(n)]
# for i in range(n):
#     play_list[i] = 60*int(play_list[i][0]) + int(play_list[i][1])
# answer = []
# for i in range(n):
#     temp = my_time
#     for j in range(i, n):
#         temp -= play_list[j]
#         if temp <= 0:
#             answer.append([j-i+1, i+1])
#             break
# answer = sorted(answer, key=lambda x : (-x[0], x[1]))
# print(*answer[0])

#----------------------------------------------------------------
# from itertools import combinations
# def search(u):
#     if u != node_set[u]:
#         node_set[u] = search(node_set[u])
#     return node_set[u]
# def union(u, v):
#     r1 = search(u)
#     r2 = search(v)
#     node_set[r2] = r1
# n = int(input()) # 리소스수 = (도시수-1)! 즉, 예시에 리소스 정보가 6이면 도시의 수는 4(3! = 6)
# resource_info = [list(input().split()) for _ in range(n)]
# resource_info = sorted(resource_info, key=lambda x: int(x[2]))
# city_num = 0
# dp = [0 for _ in range(n)]
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n):
#     dp[i] = dp[i-1] * i
#     if dp[i] == n:
#         city_num = i+1
#         break
# graph = []
# node_set = [0]
# temp_set = set()
# for i in range(1, city_num+1):
#     temp_set.add(resource_info[i][0])
#     temp_set.add(resource_info[i][1])
# temp_set = list(temp_set)
# for i in range(city_num):
#     node_set.append(temp_set[i])
# edges = 0
# cost = 0
# while True:
#     if edges == n-1:
#         break
#     u, v, w = resource_info.pop(0)
#     if search(u) != search(v):
#         union(u, v)
#         graph.append((u,v))
#         cost += w
#         edges += 1
# print(graph)
# print(cost)

#---------------------------------------------------------------------------------------
# from collections import deque
# n, q = map(int, input().split())
# tree = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     parent, child = map(int, input().split())
#     tree[parent].append(child)
# for _ in range(q):
#     parent, child = map(int, input().split())
#     if child in tree[parent]:
#         print('yes')
#     elif not tree[parent]:
#         print('no')
#     else:
#         queue = deque()
#         queue.append(parent)
#         visited = [0 for _ in range(n+1)]
#         visited[parent] = 1
#         while queue:
#             current_node = queue.popleft()
#             for i in tree[current_node]:
#                 if i == child:
#                     break
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     queue.append(i)
#             else:
#                 continue
#             print('yes')
#             break
#         else:
#             print('no')






#----------------------------------------------------------------------------------------
# import sys
# n = int(sys.stdin.readline())
# words = [sys.stdin.readline().strip() for _ in range(n)]
# q = int(sys.stdin.readline())
# search_words = [sys.stdin.readline().strip() for _ in range(q)]
# for i in search_words:
#     temp = " ".join(words)
#     answer = 0
#     if i not in temp:
#         print(0)
#     else:
#         while True:
#             search_idx = temp.index(i)
#             temp = temp[:search_idx] + temp[search_idx+len(i):]
#             answer += 1
#             if i not in temp:
#                 break
#         print(answer)




