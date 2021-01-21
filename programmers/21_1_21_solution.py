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




# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3


# def solution(n, words):
#     answer = []
#     used = []
#     cycle = 0
#     fail_person = 0
#     for i,p in enumerate(words):
#         if (i+1) % n == 1:
#             cycle += 1
#         if used.count(p) == 0:
#             if i != 0 and used[-1][-1:] != p[:1]:
#                 fail_person = (i+1) % n
#                 if fail_person == 0:
#                     fail_person = n
#                 break
#             used.append(p)
#         else:
#             fail_person = (i+1) % n
#             if fail_person == 0:
#                 fail_person = n
#             break
#     else:
#         return [0,0]
#     return [fail_person,cycle]
