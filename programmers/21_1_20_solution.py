# https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3

# def solution(arr):
#     arr.sort()
#     max = arr.pop()
#     multiple_num = 1
#     while True:
#         count = 0
#         temp = max * multiple_num 
#         for i in arr:
#             if temp % i ==0:
#                 count += 1
#         if count == len(arr):
#             return temp
#         multiple_num += 1    
#     
#       다른 사람 풀이
# from fractions import gcd


# def solution(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer




# https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3

# def solution(arr1, arr2):
#     answer = []
#         for idx1 in range(len(arr1)):
#         row = []
#         for idx2 in range(len(arr2[0])):
#             tmp = 0
#             for idx3 in range(len(arr1[0])):
#                 tmp += arr1[idx1][idx3] * arr2[idx3][idx2]
#             row.append(tmp)
#         answer.append(row)
#     return answer



# https://www.acmicpc.net/problem/3986

# import sys
# input=sys.stdin.readline
# n=int(input())
# count=0
# for j in range(n):
#     s=input().strip()
#     stack=[]
#     for i in s:
#         if not stack or stack[-1]!=i:
#             stack.append(i)
#         else:
#             stack.pop()
#     if not stack:
#         count+=1
# print(count)



# https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3
# from itertools import combinations

# def solution(relation):
#     answer = 0
#     all = []
#     unique_list = []
#     for i in range(1, len(relation[0]) + 1):
#     # append는 런타임에러가 뜸 append와 extend 비교하여 알아둘 것
#         all.extend([set(k) for k in combinations([j for j in range(len(relation[0]))], i)])
#     for subset in all:
#         unique = True
#         row_set = set()
#         for i in range(len(relation)):
#             row = ''
#             for j in subset:
#                 row += relation[i][j]
#             if row in row_set:
#                 unique = False
#                 break
#             row_set.add(row)
#         if unique:
#             unique_list.append(subset)
#     unique_list = sorted(unique_list, key=lambda x: len(x))
#     answer_list = []
#     for subset in unique_list:
#         subset = set(subset)
#         check = True
#         for j in answer_list:
#             if j.issubset(subset):
#                 check = False
#         if check:
#             answer_list.append(subset)

#     print(answer_list)
#     return len(answer_list)
