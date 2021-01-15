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

# import re


# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}

#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)            

#     for i in range(len(dart)):                # 정규표현식으로 갈무리된 문자열들
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer



# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3


# s =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'
# now_location = [10,12]
# answer = ''
# while s:
#     push_num = s.pop(0)
#     if push_num == 1 or push_num == 4 or push_num == 7:
#         answer += 'L'
#         now_location[0] = push_num
#     elif push_num == 3 or push_num == 6 or push_num == 9:
#         answer += 'R'
#         now_location[1] = push_num
#     else:
#         push_num = 11 if push_num == 0 else push_num
#         print(push_num)
            
#         absL = abs(push_num-now_location[0])
#         absR = abs(push_num-now_location[1])
            
#         if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
#             answer+='R'
#             now_location[1] = push_num
#         elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
#             answer +='L'
#             now_location[0] = push_num
#         else:
#             if hand == 'left':
#                 answer+='L'
#                 now_location[0] = push_num
#             else:
#                 answer+='R'
#                 now_location[1] = push_num
# print(answer)