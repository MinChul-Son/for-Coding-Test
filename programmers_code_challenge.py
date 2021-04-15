# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i]:
#             answer += absolutes[i]
#         else:
#             answer -= absolutes[i]
#     return answer

#-------------------------------------------------
# from collections import deque
# def solution(s):
#     answer = 0
#     s = deque(s)
#     for i in range(len(s)):
#         small = 0
#         medium = 0
#         big = 0
#         for j in s:
#             if j == '(':
#                 small += 1
#             elif j == ')':
#                 small -= 1
#             elif j == '{':
#                 medium += 1
#             elif j == '}':
#                 medium -= 1
#             elif j == '[':
#                 big += 1
#             elif j == ']':
#                 big -= 1
            
#             if small < 0 or medium < 0 or big < 0:
#                 break
#         else:
#             if small % 2 == 0 and medium % 2 == 0 and big % 2 == 0:
#                 answer += 1
#         s.rotate(-1)

#     return answer

#-------------------------------------------------------------------------
# def solution(a, edges):
#     if a.count(0) == len(a):
#         return 0 
#     if sum(a):
#         return -1
#     answer = 0
    
#     return answer

# solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])
