# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
# def solution(s):
#     s = list(s)
#     temp_list = []
#     for i in range(len(s)):
#         temp_list.append(s.pop(0))
#         if len(temp_list) >= 2:
#             if temp_list[-1] == temp_list[-2]:
#                 temp_list.pop()
#                 temp_list.pop()
#     if temp_list:
#         return 0
#     else:
#         return 1



# def solution(s):
#     answer = 0
#     temp_list = []
#     for i in s:
#         temp_list.append(i)
#         if len(temp_list) == 1:
#             continue
#         if temp_list[-1] == temp_list[-2]:
#             temp_list.pop()
#             temp_list.pop()
#     return 1 if not temp_list else 0

# print(solution('baabaa'))







# https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3

# def solution(n,a,b):
#     count = 1 
#     while abs(a-b) != 1:
#         count += 1
#         if a % 2 ==0:
#             a = a // 2
#         else:
#             a = a // 2 + 1
#         if b % 2 ==0:
#             b = b // 2
#         else:
#             b = b // 2 + 1
#     return count



# def solution(n,a,b):
#     count = 0
#     while a != b:
#         count += 1
#         a = (a+1) // 2
#         b = (b+1) // 2
#     return count
# print(solution(8,4,7))

# def solution(n,a,b):
#     count = 1 
#     if a > b:
#         a, b = b, a
#     if a % 2 and abs(a-b) == 1:
#         return count
#     while True:
#         count += 1
#         if a % 2 ==0:
#             a = a // 2
#         else:
#             a = a // 2 + 1
#         if b % 2 ==0:
#             b = b // 2
#         else:
#             b = b // 2 + 1
#         if a % 2 and abs(a-b) == 1:
#             return count