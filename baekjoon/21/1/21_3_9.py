# https://www.acmicpc.net/problem/1011
# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)


# https://www.acmicpc.net/problem/9020
# t = int(input())
# # n이하의 소수 구하여 조합하기
# primes = [0 for i in range(10001)]
# primes[1] = 1
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         primes[j] = 1
# for _ in range(t):
#     a = int(input())
#     b = a // 2
#     for j in range(b, 1, -1):
#         if primes[a - j] == 0 and primes[j] == 0:
#             print(j, a - j)
#             break


# https://www.acmicpc.net/problem/1149
# n = int(input())
# color_cost = []
# for _ in range(n):
#     color_cost.append(list(map(int, input().split())))
# for i in range(1, n):
#     color_cost[i][0] = min(color_cost[i-1][1], color_cost[i-1][2]) + color_cost[i][0]
#     color_cost[i][1] = min(color_cost[i-1][0], color_cost[i-1][2]) + color_cost[i][1]
#     color_cost[i][2] = min(color_cost[i-1][0], color_cost[i-1][1]) + color_cost[i][2]
# print(min(color_cost[-1]))


# https://www.acmicpc.net/problem/12865
# n, k = map(int, input().split())
# dp = [[0] * (k + 1) for i in range(n + 1)]
# w = [0]
# v = [0]
# for _ in range(n):
#     w_, v_ = map(int, input().split())
#     w.append(w_)
#     v.append(v_)
# for i in range(1, n + 1):
#     for j in range(k, 0, - 1):
#         if j - w[i] >= 0:
#             dp[i][j] = max(dp[i - 1][j], v[i] + dp[i - 1][j - w[i]])
#         else:
#             dp[i][j] = dp[i - 1][j]
# print(max(dp[n]))



# https://www.acmicpc.net/problem/2407
from math import factorial
n, m = map(int, input().split())
print(factorial(n)//(factorial(n-m) * factorial(m)))


