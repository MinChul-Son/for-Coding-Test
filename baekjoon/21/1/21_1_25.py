# https://www.acmicpc.net/problem/2798
# from itertools import combinations
# n, m = map(int,input().split())
# card_list = list(map(int,input().split()))
# combi = list(combinations(card_list,3))
# answer = 0
# for i in combi:
#     if sum(i) <= m and answer < sum(i):
#         answer = sum(i)
# print(answer)

# https://www.acmicpc.net/problem/2231
# n = int(input())
# answer = 0
# for i in range(1,n+1):
#     temp = list(map(int,str(i)))
#     answer = i + sum(temp)
#     if answer == n:
#         print(i)
#         break
#     if i == n:
#         print(0)