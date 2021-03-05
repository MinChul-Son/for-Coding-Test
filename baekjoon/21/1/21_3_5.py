# https://www.acmicpc.net/problem/2644
# import sys
# from collections import deque
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visit = [0 for i in range(n + 1)]
#     visit[start] = 1
#     while queue:
#         d = queue.popleft()
#         for i in tree[d]:
#             if visit[i] == 0:
#                 visit[i] = 1
#                 result[i] = result[d] + 1
#                 queue.append(i)
# n = int(sys.stdin.readline())
# cal_num1, cal_num2 = map(int, sys.stdin.readline().split())
# m = int(sys.stdin.readline())
# tree = [[] for _ in range(n+1)]
# result = [0 for i in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     tree[a].append(b)
#     tree[b].append(a)
# bfs(cal_num1)
# print(result[cal_num2] if result[cal_num2] != 0 else -1)


# https://www.acmicpc.net/problem/2312
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     child_list = []
#     devide_num = 2
#     while n != 1:
#         count = 0
#         while True:
#             if n % devide_num == 0:
#                 n //= devide_num
#                 count += 1
#             else:
#                 break
#         child_list.append([devide_num, count])
#         devide_num += 1
#     for i in child_list:
#         if i[1]:
#             print(*i)



# https://www.acmicpc.net/problem/10826
n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


