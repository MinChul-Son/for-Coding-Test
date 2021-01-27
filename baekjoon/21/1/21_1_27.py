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


# https://www.acmicpc.net/problem/1436

# n = int(input())
# answer = 0
# count = 0
# while True:
#     temp = str(answer)
#     if '666' in temp:
#         count += 1
#     if count == n:
#         break
#     answer += 1
# print(answer)

# https://www.acmicpc.net/problem/2750
# n = int(input())
# N = list(int(input()) for _ in range(n))
# N.sort()
# for i in N:
#     print(i)

# https://www.acmicpc.net/problem/2751
# n = int(input())
# N = list(int(input()) for _ in range(n))
# for i in sorted(N):
#     print(i)

# https://www.acmicpc.net/problem/10989

# import sys
# n = int(sys.stdin.readline())
# numbers = [0 for _ in range(10000)]
# for _ in range(n):
#     numbers[int(sys.stdin.readline())-1] += 1
# for i in range(10000):
#     if numbers[i] > 0:
#         sys.stdout.write((str(i+1) +'\n')*numbers[i])


# https://www.acmicpc.net/problem/2108
# import sys
# import math
# from collections import Counter

# n = int(input())
# N = [int(sys.stdin.readline()) for _ in range(n)]
# if n == 1:
#     print(N[0])
#     print(N[0])
#     print(N[0])
#     print(0)
# else:
#     N.sort()
#     cnt = Counter(N)
#     cnt = cnt.most_common()
#     print(round(sum(N)/n))
#     print(N[n//2])
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
#     print(max(N)-min(N))


# https://www.acmicpc.net/problem/1427
# n = int(input())
# n =list(map(int,list(str(n))))
# n = sorted(n, reverse=True)
# print(int("".join(list(map(str,n)))))


# https://www.acmicpc.net/problem/11650
# from operator import itemgetter
# n = int(input())
# N = list(tuple(map(int,input().split())) for _ in range(n))
# N = sorted(N, key=itemgetter(0,1))
# for i in N:
#     print(i[0],i[1])


# https://www.acmicpc.net/problem/11651

# from operator import itemgetter
# n = int(input())
# N = list(tuple(map(int,input().split())) for _ in range(n))
# N = sorted(N, key=itemgetter(1,0))
# for i in N:
#     print(i[0],i[1])

# https://www.acmicpc.net/problem/1181
# import sys
# n = int(input())
# N = list(sys.stdin.readline().strip() for _ in range(n))
# N = list(set(N))
# N = sorted(N, key=lambda x: (len(x),x))
# for i in N:
#     print(i)


# https://www.acmicpc.net/problem/10814
# import sys
# n = int(input())
# N = list((sys.stdin.readline().split()) for _ in range(n))
# N = sorted(N, key=lambda x:int(x[0]))
# for i in N:
#     print(" ".join(i))


# https://www.acmicpc.net/problem/15649
# from itertools import permutations
# n ,m = map(int,input().split())
# num_list = [i for i in range(1,n+1)]
# permu_list = list(permutations(num_list,m))
# for i in permu_list:
#     print(" ".join(map(str,i)))

# https://www.acmicpc.net/problem/15650
# from itertools import combinations
# n ,m = map(int,input().split())
# num_list = [i for i in range(1,n+1)]
# combi_list = list(combinations(num_list,m))
# for i in combi_list:
#     print(" ".join(map(str,i)))


# https://www.acmicpc.net/problem/15651
# from itertools import product
# n ,m = map(int,input().split())
# num_list = [i for i in range(1,n+1)]
# for num in product(num_list, repeat=m):
#     for i in num:
#         print(i, end=" ")
#     print("")

# https://www.acmicpc.net/problem/15652
# import itertools
# n ,m = map(int,input().split())
# num_list = [i for i in range(1,n+1)]
# for num in itertools.combinations_with_replacement(num_list, m):
#     for i in num:
#         print(i, end=" ")
#     print("")


# https://www.acmicpc.net/problem/14888
# import sys
# from itertools import permutations
# n = int(input())
# num_list = list(map(int,input().split()))
# sign_list = list(map(int,input().split()))
# temp_list = []
# max = -sys.maxsize - 1
# min = sys.maxsize
# if sign_list[0]>0:
#     for _ in range(sign_list[0]):
#         temp_list.append('+')
# if sign_list[1]>0:
#     for _ in range(sign_list[1]):
#         temp_list.append('-')
# if sign_list[2]>0:
#     for _ in range(sign_list[2]):
#         temp_list.append('*')
# if sign_list[3]>0:
#     for _ in range(sign_list[3]):
#         temp_list.append('//')
# sign_list = list(set(list(permutations(temp_list,n-1))))
# for i in sign_list:
#     temp_list = num_list.copy()
#     idx = -1
#     print(temp_list,num_list)
#     result = temp_list.pop(0)
#     while temp_list:
#         idx += 1
#         next_num = temp_list.pop(0)
#         current_cal = i[idx]
#         if current_cal == '+':
#             result += next_num
#         elif current_cal == '-':
#             result -= next_num
#         elif current_cal == '*':
#             result *= next_num
#         else:
#             if result < 0:
#                 result = -(result)
#                 result //= next_num
#                 result = -(result)
#             else:
#                 result //= next_num
#     if result < min:
#         min = result
#     if max< result:
#         max = result
# print(max,min)



