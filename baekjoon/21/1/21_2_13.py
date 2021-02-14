# https://www.acmicpc.net/problem/11051
# from math import factorial
# n, k = map(int, input().split())
# result = factorial(n) // (factorial(k) * factorial(n - k))
# print(result % 10007)

# https://www.acmicpc.net/problem/9375
# import sys
# t = int(input())
# for _ in range(t):
#     answer = 1
#     kinds = []
#     n = int(input())
#     cloth = [sys.stdin.readline().split() for _ in range(n)]
#     for i in cloth:
#         count = 0
#         temp = []
#         for j in range(len(cloth)):
#             if i[1] == cloth[j][1]:
#                 count += 1
#         temp.append(count)
#         temp.append(i[1])
#         if kinds.count(temp) == 0:
#             kinds.append(temp)
#             answer = answer * (temp[0]+1)
#         else:
#             pass
#     answer -= 1
#     print(answer)

# https://www.acmicpc.net/problem/1676
# from math import factorial
# n = int(input())
# fac = list(str(factorial(n)))
# fac.reverse()
# count = 0
# for i in fac:
#     if i == '0':
#         count += 1
#     else:
#         break
# print(count)