# def solution(n,record):
#     answer = []
#     temp_list = sorted(record, key=lambda x: x[0])
#     print(temp_list)
#     check_server = '1'
#     temp = []
#     for i in temp_list:
#         s =i.split(" ")
#         if s[0] == check_server:
#             if s[1] in temp:
#                 continue
#             if len(temp) <5:
#                 temp.append(s[1])
#             else:
#                 temp.pop(0)
#                 temp.append(s[1])
#         else:
#             answer.extend(temp)
#             check_server = i[0]
#             temp = []
#             temp.append(s[1])
#     answer.extend(temp)
#     print(answer)
#     return answer

# solution(4,["1 fracta", "1 sina", "1 hana","1 robel", "1 abc", "1 sina", "1 lynn"])



# def solution(m, v):
#     answer = 0
#     game_list = []
#     for i in v:
#         if not game_list:
#             game_list.append(i)
#         else:           
#             for j,p in enumerate(game_list):
#                 if m-p >= i:
#                     game_list[j] += i
#                     break
#                 else:
#                     continue
#             else:
#                 game_list.append(i)
#     print(game_list)
    
#     return len(game_list)

# print(solution(4,[3,2,3,1]))


#배열을 연결리스트로 표현한 것과 비슷
#하나씩 뽑아서 값을 보고 인덱스를 쫓아들어감. 그 떄마다 count +1 해서 나중에 max값
# from operator import itemgetter, attrgetter

# def solution(next_student):
#     count_list = []
#     for i,p in enumerate(next_student):
#         if p == 0 :
#             count_list.append((i+1,1))
#         else:
#             student_num = p
#             count = 1
#             temp_list = [i+1]
#             while True:
#                 if next_student[student_num-1] != 0:
#                     if student_num not in temp_list:
#                         count += 1
#                         temp_list.append(student_num)
#                         student_num = next_student[student_num-1]
#                     else:
#                         count_list.append((count,i+1))
#                         break
#                 else:
#                     count += 1
#                     count_list.append((count,i+1))
#                     break
#     answer = sorted(count_list, key=itemgetter(0,1))
#     return answer[-1][1]

# print(solution([5,9,13,1,0,0,11,1,7,12,9,9,2]))