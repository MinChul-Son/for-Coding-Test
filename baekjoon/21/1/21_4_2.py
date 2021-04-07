# # https://www.acmicpc.net/problem/3190
# import sys
# from collections import deque
# input = sys.stdin.readline
# def changedir(cha):
#     if cha == "L":
#         if direction == [1, 0]:
#             return [0, 1]
#         elif direction == [-1, 0]:
#             return [0, -1]
#         elif direction == [0, 1]:
#             return [-1, 0]
#         elif direction == [0, -1]:
#             return [1, 0]
#     elif cha == "D":
#         if direction == [1, 0]:
#             return [0, -1]
#         elif direction == [-1, 0]:
#             return [0, 1]
#         elif direction == [0, 1]:
#             return [1, 0]
#         elif direction == [0, -1]:
#             return [-1, 0]
# def check(x, y):
#     if [x, y] in q:
#         return False
#     return True
# n = int(input())
# s = [[0] * (n + 1) for i in range(n + 1)]
# k = int(input())
# for i in range(k):
#     a, b = map(int, input().split())
#     s[a][b] = 1
# l = int(input())
# d = deque()
# for i in range(l):
#     a, b = input().split()
#     d.append([int(a), b])
# direction = [0, 1]
# q = deque()
# q.append([1, 1])
# cnt = 0
# while True:
#     x, y = q[-1][0], q[-1][1]
#     x += direction[0]
#     y += direction[1]
#     if 0 < x <= n and 0 < y <= n:
#         if not check(x, y):
#             break
#         q.append([x, y])
#         if s[x][y] == 1:
#             s[x][y] = 0
#         else:
#             q.popleft()
#     else:
#         break
#     cnt += 1
#     if d and cnt == d[0][0]:
#         direction = changedir(d[0][1])
#         d.popleft()
# print(cnt + 1)



# https://www.acmicpc.net/problem/1976
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 1
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(m-1):
    if graph[plan[i]-1][plan[i+1]-1] != 1:
        print('NO')
        break
else:
    print('YES')
