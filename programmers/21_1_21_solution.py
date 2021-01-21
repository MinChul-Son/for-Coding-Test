# https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3

# def solution(n):
#     answer = 1
#     for i in range(1,n//2+1):
#         count = 0
#         for j in range(i, n+1):
#             count += j
#             if count == n:
#                 answer += 1
#                 break
#             elif count > n:
#                 break
#     return answer



# https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

# def solution(s):
#     answer = s.split(" ")
#     for i,p in enumerate(answer):
#         if p[:1].isalpha():
#             answer[i] = p[:1].upper() + p[1:].lower()
#         else:
#             answer[i] = p[:1] + p[1:].lower()
#     return " ".join(answer)




# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3


# def solution(n, words):
#     answer = []
#     used = []
#     cycle = 0
#     fail_person = 0
#     for i,p in enumerate(words):
#         if (i+1) % n == 1:
#             cycle += 1
#         if used.count(p) == 0:
#             if i != 0 and used[-1][-1:] != p[:1]:
#                 fail_person = (i+1) % n
#                 if fail_person == 0:
#                     fail_person = n
#                 break
#             used.append(p)
#         else:
#             fail_person = (i+1) % n
#             if fail_person == 0:
#                 fail_person = n
#             break
#     else:
#         return [0,0]
#     return [fail_person,cycle]




# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3

# mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
# new_list = list(map(list, zip(*mylist)))
# print(new_list)
# import itertools

# def solution(board):
#     M, N = len(board), len(board[0])
#     for i in range(1, M):
#         for j in range(1, N):
#             if board[i][j] == 1:
#                 board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
#                 print(board)

#     return max(itertools.chain(*board))**2

# solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
