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

# #현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-1,2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# #8가지 방향에 대해 각 위치로 이동이 가능한지 확인
# result = 0 
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
#         result += 1
# print(result)

# s = input()
# alpha_list = []
# num_list = []
# for i in s:
#     if i.isalpha():
#         alpha_list.append(i)
#     else:
#         num_list.append(i)
# alpha_list.sort()
# answer = "".join(alpha_list) + str(sum(map(int,num_list)))
# print(answer)