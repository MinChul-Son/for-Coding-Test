# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3


# s = '1S2D*3T'
# s = list(s)
# temp_list = []
# for i,p in enumerate(s):
#     if p.isdigit():
#         if s[i-1].isdigit():
#             continue
#         temp_str =""
#         for j in range(i,len(s)):
#             if s[j].isdigit():
#                 if i ==j:
#                     temp_str += s[j]
#                 else:
#                     if j-i ==1:
#                         print(temp_str)
#                         temp_str += s[j]
#                         print(temp_str)
#                     else:
#                         temp_list.append(temp_str)
#                         break
#             else:
#                 temp_str += s[j]
# temp_list.append(temp_str)
# print(temp_list)
# answer_list = [0] * len(temp_list)
# for i in range(len(temp_list)):
#     change_list = list(temp_list.pop(0))
#     temp= 0
#     for j in range(len(change_list)):
#         if s[j-1].isdigit():
#             continue
#         if change_list[j].isdigit():
#             if change_list[j+1].isdigit():
#                 temp = int(change_list[j]+change_list[j+1])
#                 print(temp)
#             else:
#                 temp = int(change_list[j])
#         elif change_list[j].isalpha():
#             if change_list[j] == 'S':
#                 pass
#             elif change_list[j] == 'D':
#                 temp = temp ** 2
#             else:
#                 temp = temp **3
#         else:
#             if change_list[j] =='*':
#                 if i ==0:
#                     temp = temp *2
#                 else:
#                     temp = temp *2
#                     answer_list[i-1] = answer_list[i-1] * 2

#             else:
#                 temp = temp *(-1)
#     answer_list[i] += temp
# print(sum(answer_list))

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)            

    for i in range(len(dart)):                # 정규표현식으로 갈무리된 문자열들
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
        



        

        