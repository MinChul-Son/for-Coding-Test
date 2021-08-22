# def solution(infos, actions):
#     answer = []
#     is_login = False
#     cart = []
#     for i in actions:
#         split_list = i.split(" ")
#         if split_list[0] == "LOGIN":
#             if is_login:
#                 answer.append(False)
#                 continue
#             if split_list[1] +" " + split_list[2] not in infos:
#                 answer.append(False)
#                 continue
#             is_login = True
#             answer.append(True)

#         elif split_list[0] == "ADD":
#             if not is_login:
#                 answer.append(False)
#                 continue
#             cart.append(split_list[1])
#             answer.append(True)
#         else:
#             if not cart:
#                 answer.append(False)
#                 continue
#             cart.clear()
#             answer.append(True)

#     return answer


#---------------------------------------------------------
# def solution(grades):
#     grade = {
#         'A+' : 13, 
#         'A0' : 12,
#         'A-' : 11,
#         'B+' : 10,
#         'B0' : 9,
#         'B-' : 8,
#         'C+' : 7,
#         'C0' : 6,
#         'C-' : 5,
#         'D+' : 4,
#         'D0' : 3,
#         'D-' : 2,
#         'F' : 1
#     }

#     score_board = dict()

#     answer = []
#     temp_answer = []
#     for i in grades:
#         split_list = i.split(" ")

#         if split_list[0] in score_board:
#             if grade[split_list[1]] > grade[score_board[split_list[0]]]:
#                 temp_answer.remove([split_list[0], score_board[split_list[0]]])
#                 score_board[split_list[0]] = split_list[1]
#                 temp_answer.append(split_list)
#             continue

#         score_board[split_list[0]] = split_list[1]
#         temp_answer.append(split_list)
    
#     temp_answer = sorted(temp_answer, key= lambda x: x[1])

#     for i in temp_answer:
#         answer.append(" ".join(i))
#     return answer

# solution(["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"])

#-----------------------------------------------------
import copy
def solution(word, cards):
    if len(word) > len(cards):
        return 0
    answer = 0
    

    return answer

solution("APPLE", ["LLZKE", "LCXEA","CVPPS","EAVSR","FXPFP"])


#----------------------------------------------------


# SQL 문제


# SELECT EMPLOYEE_ID, 
# (CASE
#     WHEN COUNT(EMPLOYEE_ID) >= 4 THEN '최우수 사원'
#     WHEN COUNT(EMPLOYEE_ID) >= 2 THEN '우수 사원'
#     ELSE '일반 사원'
# END) AS '분류 상태', 
# COUNT(EMPLOYEE_ID) AS COUNT FROM SELLINGS
# GROUP BY EMPLOYEE_ID
# ORDER BY EMPLOYEE_ID;