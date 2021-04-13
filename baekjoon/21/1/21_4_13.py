# https://www.acmicpc.net/problem/1351
# from collections import defaultdict
# import sys
# def dp(n):
#     if data[n] != 0:
#         return data[n]
#     data[n] = dp(n // p) + dp(n // q)
#     return data[n]
# input = sys.stdin.readline
# n, p, q = map(int, input().split())
# data = defaultdict(int)
# data[0] = 1
# print(dp(n))


# https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[1] = 1
for i in range(1, k + 1):
    a = []
    for j in coins:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
print(dp[k])