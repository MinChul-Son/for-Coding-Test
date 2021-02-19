# https://www.acmicpc.net/problem/1927
# import heapq
# import sys
# n = int(input())
# queue = []
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     if x != 0:
#         heapq.heappush(queue,x)
#     else:
#         if not queue:
#             print(0)
#         else:
#             print(heapq.heappop(queue))



# https://www.acmicpc.net/problem/1406
# import sys
# s = sys.stdin.readline().strip()
# m = int(input())
# order_list = [sys.stdin.readline().split() for _ in range(m)]
# current_idx = len(s)
# for i in order_list:
#     if i[0] == 'L':
#         if current_idx == 0:
#             continue
#         else:
#             current_idx -= 1
#     elif i[0] == 'D':
#         if current_idx == len(s):
#             continue
#         else:
#             current_idx += 1
#     elif i[0] == 'B':
#         if current_idx == 0:
#             continue
#         else:
#             s = s[0:current_idx-1] + s[current_idx:]
#             current_idx -= 1
#     else:
#         s = s[0:current_idx] + i[1] + s[current_idx:]
#         current_idx += 1
# print(s)



# import sys 
# left_stack = list(sys.stdin.readline()[:-1]) 
# right_stack = list() 
# testcase = int(sys.stdin.readline()) 
# for _ in range(testcase): 
#     cmd = sys.stdin.readline() 
#     if cmd[0] == 'L' and left_stack: 
#         right_stack.append(left_stack.pop()) 
#     elif cmd[0] == 'D' and right_stack: 
#         left_stack.append(right_stack.pop()) 
#     elif cmd[0] == 'B' and left_stack: 
#         left_stack.pop() 
#     elif cmd[0] == 'P': 
#         left_stack.append(cmd[2]) 
# sys.stdout.write(''.join(left_stack + right_stack[::-1]))




# https://www.acmicpc.net/problem/10816
# from bisect import bisect_left, bisect_right
# n = int(input())
# my_card = sorted(list(map(int, input().split())))
# m = int(input())
# num_card = list(map(int, input().split()))
# for i in num_card:
#     print(bisect_right(my_card, i) - bisect_left(my_card, i), end=" ")



# https://www.acmicpc.net/problem/1021
# from collections import deque
# n, m = map(int, input().split())
# queue = deque([i for i in range(1, n+1)])
# pop_list = list(map(int, input().split()))
# count = 0
# for i in pop_list:
#     while True:
#         if queue[0] == i:
#             queue.popleft()
#             break
#         else:
#             if queue.index(i) <= len(queue)//2:
#                 queue.rotate(-1)
#                 count += 1
#             else:
#                 queue.rotate(1)
#                 count += 1
# print(count)



# https://www.acmicpc.net/problem/11279
import sys
import heapq
n = int(input())
queue = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
    else:
        heapq.heappush(queue, (-x, x))







