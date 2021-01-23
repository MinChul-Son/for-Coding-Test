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


