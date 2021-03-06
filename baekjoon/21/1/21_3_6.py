# https://www.acmicpc.net/problem/10844
# n = int(input())
# dp = [[0 for i in range(10)] for j in range(101)]
# for i in range(1, 10):
#     dp[1][i] = 1
# for i in range(2, n + 1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i - 1][1]
#         elif j == 9:
#             dp[i][j] = dp[i - 1][8]
#         else:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
# print(sum(dp[n]) % 1000000000)



# https://www.acmicpc.net/problem/1120
a, b = input().split()
b = list(b)
len_a = len(a)
max_cnt = 0
while len_a <= len(b):
    cnt = 0
    for i in range(len_a):
        if a[i] == b[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    print(a,b)
    del b[0]
print(len_a - max_cnt)