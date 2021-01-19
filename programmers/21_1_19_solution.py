# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
# import re
# from itertools import permutations

# def solution(expression):
#     expressions = set(re.findall("\D", expression))
#     prior = permutations(expressions)
#     cand = []

#     for op_cand in prior:
#         temp = re.compile("(\D)").split('' + expression)
#         print(temp)
#         for exp in op_cand:
#             while exp in temp:
#                 idx = temp.index(exp)
#                 temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
#         cand.append(abs(int(temp[0])))
#     return max(cand)

# print(solution("100-200*300-500+20"))




# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3

# def solution(m, n, board):
#     answer = 0
    
#     board = list(map(list,board))
#     loop_check = True
#     while loop_check:
#         temp = []
#         for i in range(m-1):
#             for j in range(n-1):
#                 compare_str = board[i][j]
#                 if compare_str == 0:
#                     pass
#                 else:
#                     if compare_str == board[i+1][j]:
#                         if compare_str == board[i][j+1] and compare_str == board[i+1][j+1]:
#                             temp.append((i,j))
#         if not temp:
#             break

#         for i in temp: #boom
#             if board[i[0]][i[1]] != 0:
#                 board[i[0]][i[1]] = 0
#                 answer +=1
#             if board[i[0]+1][i[1]] != 0:
#                 board[i[0]+1][i[1]] = 0
#                 answer +=1
#             if board[i[0]][i[1]+1] != 0:
#                 board[i[0]][i[1]+1] = 0
#                 answer +=1
#             if board[i[0]+1][i[1]+1] != 0:
#                 board[i[0]+1][i[1]+1] = 0
#                 answer +=1
#         for k in range(m-1):
#             for i in range(1,m):
#                 for j in range(n):
#                     if board[i][j] == 0:
#                         board[i][j] = board[i-1][j]
#                         board[i-1][j] = 0    
#     return answer

