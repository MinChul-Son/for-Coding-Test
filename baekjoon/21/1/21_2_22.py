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

# https://www.acmicpc.net/problem/1912
# n = int(input())
# n_list = list(map(int, input().split()))
# dp = [0 for _ in range(n)]
# for i in range(1, n-1):
#     dp[i] = max(dp[i-1], n_list[i-1], n_list[i-1]+dp[i-1])
# print(dp)

# n = int(input())
# a = list(map(int, input().split()))
# sum = [a[0]]
# for i in range(n - 1):
#     sum.append(max(sum[i] + a[i + 1], a[i + 1]))
# print(max(sum))



# https://www.acmicpc.net/problem/2748
# n = int(input())
# dp = [0 for _ in range(n+1)]
# dp[1] = 1
# for i in range(2, n+1):
#     dp[i] = dp[i-2] + dp[i-1]
# print(dp[n])


# https://www.acmicpc.net/problem/11055
# n = int(input())
# lst = list(map(int, input().split()))

# dp = [x for x in lst]

# for i in range(n):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + lst[i])
# print(max(dp))


# https://www.acmicpc.net/problem/11722

# n = int(input())
# n_list = list(map(int, input().split()))

# dp = [1 for _ in range(n)]

# for i in range(n):
#     for j in range(i):
#         if n_list[i] < n_list[j]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))


