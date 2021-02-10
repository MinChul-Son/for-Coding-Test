# https://www.acmicpc.net/problem/4948

# while True:
#     m = int(input())
#     if m == 0:
#         break
#     elif m == 1:
#         print(1)
#     else:
#         n = 2*m 
#         count = 0
#         num_list = [True for _ in range(n)]
#         for i in range(2, int(n**0.5) + 1):
#             if num_list[i] == True:
#                 for j in range(2*i, n, i):
#                     num_list[j] = False
#         for i in range(m+1, n):
#             if i >1 and num_list[i] == True:
#                 count += 1
#         print(count)


# https://www.acmicpc.net/problem/1085
# x, y, w, h = map(int, input().split())
# print(min(x,y,w-x,h-y))

# https://www.acmicpc.net/problem/3009
# point_x = []
# point_y = []
# for i in range(3):
#         x, y = map(int, input().split())
#         point_x.append(x)
#         point_y.append(y)
# for i in range(3):
#         if point_x.count(point_x[i]) == 1:
#                 x = point_x[i]
#         if point_y.count(point_y[i]) == 1:
#                 y = point_y[i]
# print(x, y)


# https://www.acmicpc.net/problem/4153
# while True:
#     x = list(map(int, input().split()))
#     if x[0] == 0 and x[1] == 0 and x[2] == 0:
#         break
#     x.sort()
#     if ((x[0]**2) + (x[1]**2)) == (x[2]**2):
#         print('right')
#     else:
#         print('wrong')

# https://www.acmicpc.net/problem/3053
# import math
# r = int(input())
# print(r*r*math.pi)
# print(r*r*2)


# https://www.acmicpc.net/problem/1002
# t = int(input())
# for _ in range(t):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     rs = r1 + r2
#     rm = abs(r1 - r2)
#     if d == 0:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if d == rs or d == rm:
#             print(1)
#         elif d < rs and d > rm:
#             print(2)
#         else:
#             print(0)
