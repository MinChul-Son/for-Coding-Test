# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

# def solution(cacheSize, cities):
#     answer = 0
#     cache_list = []
#     if cacheSize > 0:
#         for i in cities:
#             if cache_list.count(i.upper()) == 0: #cache_miss
#                 answer += 5
#                 if len(cache_list) == cacheSize:
#                     cache_list.pop(0)
#                     cache_list.append(i.upper())
#                 else:
#                     cache_list.append(i.upper())
#             else: #cache_hit
#                 answer += 1
#                 cache_list.pop(cache_list.index(i.upper()))
#                 cache_list.append(i.upper())

            
            
#     else:
#         return 5*len(cities)
    
#     return answer


# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

# def solution(str1, str2):
#     if not str1 and not str2:
#         return 1
#     divide1 =[str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].lower().isalpha()]
#     divide2 =[str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].lower().isalpha()]
    
#     if not divide1 and not divide2:
#         return 65536
#     entire = len(divide1) + len(divide2)
#     common = 0
#     for i in divide1:
#         if i in divide2:
#             common += 1
#             divide2.pop(divide2.index(i))
    

    
#     return int((common / (entire - common)) * 65536)

# print(solution("handshake","shake hands"))


# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
# import re
# def solution(s):
#     answer = []
#     a = s.split(',{')
#     a.sort(key = len)
#     for j in a:
#         numbers = re.findall("\d+", j)
#         for k in numbers:
#             if int(k) not in answer:
#                 answer.append(int(k))
#     return answer






