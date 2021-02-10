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
point_x = []
point_y = []
for i in range(3):
        x, y = map(int, input().split())
        point_x.append(x)
        point_y.append(y)
for i in range(3):
        if point_x.count(point_x[i]) == 1:
                x = point_x[i]
        if point_y.count(point_y[i]) == 1:
                y = point_y[i]
print(x, y)

