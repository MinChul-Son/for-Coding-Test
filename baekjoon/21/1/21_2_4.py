# https://www.acmicpc.net/problem/1010
# import math
# t = int(input())

# for _ in range(t):
#     n, m = map(int,input().split())
#     temp = math.factorial(m-n)
#     m = math.factorial(m)
#     n = math.factorial(n)
#     print(m//(n*temp))

# https://www.acmicpc.net/problem/1037
# n = int(input())
# N = list(map(int,input().split()))
# print(min(N)*max(N))

# https://www.acmicpc.net/problem/1158
# from collections import deque
# n, k = map(int,input().split())
# answer = []
# queue = deque([i for i in range(1,n+1)])
# while queue:
#     for i in range(1,k+1):
#         if i == k:
#             answer.append(queue.popleft())
#         else:
#             queue.append(queue.popleft())
# print('<'+", ".join(map(str,answer))+'>')

# https://www.acmicpc.net/problem/1316
# n = int(input())
# answer = 0
# for _ in range(n):
#     string = input()
#     used_list = []
#     temp = ''
#     for i in string:
#         if temp == '':
#             temp = i
#             used_list.append(temp)
#         elif temp == i:
#             pass
#         else:
#             if i in used_list:
#                 break
#             else:
#                 used_list.append(i)
#                 temp = i
#     else:
#         answer += 1
# print(answer)



# https://www.acmicpc.net/problem/2941

# string = input()
# alpha_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in alpha_list:
#     string = string.replace(i, '*')
# print(len(string))


# https://www.acmicpc.net/problem/1065
# n = int(input())
# answer = 0
# for i in range(1,n+1):
#     temp = str(i)
#     if len(temp) == 1 or len(temp) == 2:
#         answer += 1
#     elif len(temp) == 3:
#         if (int(temp[0]) - int(temp[1])) == (int(temp[1]) - int(temp[2])):
#             answer += 1
# print(answer)


