# https://programmers.co.kr/learn/courses/30/lessons/60057

# def solution(s):
#     length = []
#     result =""

#     for i in range(1, len(s)//2 + 1):
#         count = 1
#         temp_str = s[:i]
#         for j in range(i, len(s), i):
#             if s[j:j+i] == temp_str:
#                 count +=1
#             else:
#                 if count ==1:
#                     count =""
#                 result = result + str(count) + temp_str
#                 temp_str = s[j:j+i]
#                 count = 1
#         if count ==1:
#             count =""
#         result = result + str(count) + temp_str
#         length.append(len(result))
#         result = ""

#     return min(length)



# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor ==0:
#             answer.append(i)
#     if not answer:
#         answer.append(-1)
#     else:
#         answer.sort()
#     return answer


# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

# def solution(arr):
#     answer = []
#     for i,p in enumerate(arr):
#         if p not in answer:
#             answer.append(p)
#         elif p in answer and arr[i-1] != p:
#             answer.append(p)
#     return answer

# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
# strings = ["sun", "bed", "car"]
# n = 1
# temp_list = []
# same_list = []
# answer = []
# strings.sort()
# for i in range(len(strings)):
#     temp_list.append([strings[i][n],i])
# temp_list.sort()
# for i in range(len(temp_list)):
#     answer.append(strings[temp_list[i][1]])
# print(answer)

# def strange_sort(strings, n):
#     '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
#     return sorted(strings, key=lambda x: x[n])


# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3

# def solution(s):
#     count_p = s.count('p') + s.count('P')
#     count_y = s.count('y') + s.count('Y')
    
#     if count_p == count_y:
#         return True
#     else:
#         return False



#https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

# def solution(s):
#     ls = list(s)
#     ls.sort(reverse = True)
#     return "".join(ls)


# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

# def solution(s):
#     if len(s)== 4 or len(s)==6:
#         if s.isdecimal() == True:
#             return True
#         else:
#             return False
#     else:
#         return False


#https://programmers.co.kr/learn/courses/30/lessons/12919

# def solution(seoul):
#     answer = "김서방은 "+str(seoul.index('Kim'))+"에 있다"
#     return answer


#https://programmers.co.kr/learn/courses/30/lessons/12922

# def solution(n):
#     if n%2 ==0:
#         return "수박"*(n//2)
#     else:
#         return "수박"*(n//2) + "수"

# https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3





