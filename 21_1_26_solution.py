#동빈나 구현 알고리즘 강의


# n = int(input())
# plan_list = list(input().split())
# start_point =[1,1]

# for i in plan_list:
#     if i == 'L':
#         if start_point[1] == 1:
#             continue
#         start_point[1] -= 1
#     elif i == 'R':
#         if start_point[1] == n:
#             continue
#         start_point[1] += 1
#     elif i == 'U':
#         if start_point[0] == 1:
#             continue
#         start_point[0] -= 1
#     else:
#         if start_point[0] == n:
#             continue
#         start_point[0] += 1
# print(" ".join(map(str,start_point)))


# n = int(input())
# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
# print(count)

