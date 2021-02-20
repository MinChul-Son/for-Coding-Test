# https://www.acmicpc.net/problem/1717
# n, m = map(int, input().split())
# union_set = {i for i in range(n+1)}
# temp_list = []
# for _ in range(m):
#     input_num = list(map(int, input().split()))
#     if input_num[0] == 0:
#         if input_num[1] == input_num[2]:
#             if input_num[1] in union_set:
#                 union_set.discard(input_num[1])
#                 temp_list.append([input_num[1]])
#                 continue
#             else:
#                 continue
#         if input_num[1] in union_set and input_num[2] in union_set:
#             union_set.discard(input_num[1])
#             union_set.discard(input_num[2]) 
#             temp_list.append([input_num[1],input_num[2]])
#         elif input_num[1] in union_set:
#             for i, p in enumerate(temp_list):
#                 if input_num[2] in p:
#                     temp_list[i].append(input_num[1])
#         elif input_num[2] in union_set:
#             for i, p in enumerate(temp_list):
#                 if input_num[1] in p:
#                     temp_list[i].append(input_num[2])
#         else:
#             a_idx = 0
#             b_idx = 0
#             for i,p in enumerate(temp_list):
#                 if input_num[1] in p:
#                     a_idx = i
#                 elif input_num[2] in p:
#                     b_idx = i
#             temp_list[a_idx].extend(temp_list[b_idx])
#             temp_list.pop(b_idx)
#     else:
#         for i in temp_list:
#             if input_num[1] in i and input_num[2] in i:
#                 print("YES")
#                 break
#         else:
#             print("NO")
#     print(union_set, temp_list)



# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# parent = [ i for i in range(n + 1)]
# def find(target):
#     if target == parent[target]:
#         return target

#     parent[target] = find(parent[target])
#     return parent[target]

# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# for _ in range(m):
#     oper, a, b = map(int, input().split())
#     if oper:
#         if find(a) == find(b):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         union(a, b)
#     print(parent)



# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
t = int(input())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    temp_list = sys.stdin.readline().strip().split(",")
    if p.count('D') > n:
        print("error")
        continue
    temp_list[0] = temp_list[0][1:]
    temp_list[-1] = temp_list[-1][:-1]
    temp_list = deque(temp_list)
    for i in p:
        if i == 'R':
            temp_list.reverse()
        else:
            temp_list.popleft()
    temp_list = list(map(int, temp_list))
    print(temp_list)


