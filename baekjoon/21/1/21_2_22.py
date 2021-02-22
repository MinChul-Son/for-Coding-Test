# https://www.acmicpc.net/problem/1699

# n = int(input())
# dp = [0]*(n+1)
# for i in range(1, n+1):
#     dp[i] = i
#     j = 1
#     while j*j <= i:
#         if dp[i] > dp[i-j*j]+1:
#             dp[i] = dp[i-j*j]+1
#         j += 1
# print(dp[n])



# https://www.acmicpc.net/problem/11726
# n = int(input())

# dp = [0 for _ in range(n+1)]

# if n <= 3 : print(n)
# else : 
# 	dp[1] = 1
# 	dp[2] = 2
# 	for i in range(3, n+1):
# 		dp[i] = dp[i-1] + dp[i-2]

# 	print(dp[i]%10007)
