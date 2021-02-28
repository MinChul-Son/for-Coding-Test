# https://www.acmicpc.net/problem/2841
# import sys
# n, p = map(int, sys.stdin.readline().split())
# melody_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# stack = [[] for _ in range (7)]
# move = 0
# for i,j in melody_list:
#     if not stack[i]:
#         stack[i].append(j)
#         move += 1
#     else:
#         if j > stack[i][-1]:
#             stack[i].append(j)
#             move += 1
#         elif j == stack[i][-1]:
#             continue
#         else:
#             while stack[i] and j < stack[i][-1]:
#                 stack[i].pop()
#                 move += 1
#             if stack[i] and j == stack[i][-1]:
#                 continue
#             stack[i].append(j)
#             move += 1
# print(move)



