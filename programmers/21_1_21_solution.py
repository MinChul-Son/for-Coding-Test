# https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3

# def solution(n):
#     answer = 1
#     for i in range(1,n//2+1):
#         count = 0
#         for j in range(i, n+1):
#             count += j
#             if count == n:
#                 answer += 1
#                 break
#             elif count > n:
#                 break
#     return answer



# https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

# def solution(s):
#     answer = s.split(" ")
#     for i,p in enumerate(answer):
#         if p[:1].isalpha():
#             answer[i] = p[:1].upper() + p[1:].lower()
#         else:
#             answer[i] = p[:1] + p[1:].lower()
#     return " ".join(answer)

