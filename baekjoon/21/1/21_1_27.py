# https://www.acmicpc.net/problem/7568
# import sys
# n = int(input())
# N = list(tuple(map(int,input().split())) for _ in range(n))
# answer_list = []
# for i,p in enumerate(N):
#     count = 0
#     for j in range(n):
#         if p[0] < N[j][0] and p[1] < N[j][1]:
#             count += 1
#     answer_list.append(count+1)
# for i in answer_list:
#     print(i,end=" ")


# https://www.acmicpc.net/problem/1018

# n,m = map(int,input().split())
# board = []
# for i in range(n):
#     wb = list(map(str,input()))
#     board.append(wb)

# white_board = [['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W']]
# black_board = [['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B'], 
#             ['B','W','B','W','B','W','B','W'], 
#             ['W','B','W','B','W','B','W','B']]
# result = []

# for j in range(m-7):
#     q = 0
#     w = 0
#     for k in range(n-7):
#         count_black = 0
#         count_white = 0
#         for l in range(j,j+8):
#             for x in range(k,k+8):
#                 if board[x][l] != white_board[q][w]:
#                     count_white +=1
#                 if board[x][l] != black_board[q][w]:
#                     count_black +=1
#                 w+=1
#             w = 0
#             q+=1
#         q = 0
#         result.append(count_black)
#         result.append(count_white)
# print(min(result))


