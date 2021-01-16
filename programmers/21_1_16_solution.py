# https://programmers.co.kr/learn/courses/30/lessons/60058#qna


# def checkString(string):
#     check = 0
#     for i in string:
#         if i =='(':
#             check += 1
#         else:
#             check -= 1
#         if check < 0:
#             return False
#     else:
#         return True

# def reverse(string):
#     temp = list(string[1:-1])
#     for i in range(len(temp)):
#         if temp[i] =='(':
#             temp[i] = ')'
#         else:
#             temp[i] = '('
#     return  "".join(temp)

# def devide(string):
#     u = ''
#     v = ''
#     for i,p in enumerate(string):
#         u +=p
#         v = string[i+1:]
#         if u.count('(') == u.count(')'):
#             return u,v
    

# def recursive(string):
#     if not string:
#         return string
#     u, v = devide(string)
#     if checkString(u):
#         return u + recursive(v)
#     else:
#         return '(' + recursive(v) + ')' + reverse(u)


# def solution(p):
#     if checkString(p):
#         return p
    
#     else:
#         return recursive(p)


# https://programmers.co.kr/learn/courses/30/lessons/42885#

# def solution(people, limit):
#     boat = 0
#     s = 0
#     l =len(people)-1
#     people.sort()
#     while s<=l:
#         boat += 1
#         if people[s]+people[l] <= limit:
#             s += 1
#         l -=1
#     return boat



