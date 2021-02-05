# https://www.acmicpc.net/problem/1463
# n = int(input())
# dp = [0 for _ in range(n+1)]
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1

#     if i % 2 == 0 and dp[i] > dp[i//2] +1:
#         dp[i] = dp[i//2] + 1
#     if i % 3 == 0 and dp[i] > dp[i//3] +1:
#         dp[i] = dp[i//3] + 1
# print(dp[n])
# print(dp)

# https://www.acmicpc.net/problem/9095

# t = int(input())
# for _ in range(t):
#     dp = [1,2,4]
#     n = int(input())
#     if n <= 3:
#         print(dp[n-1])
#     else:
#         for i in range(3,n):
#             dp.append((dp[i-3]+dp[i-2]+dp[i-1]))
#         print(dp[n-1])



# https://www.acmicpc.net/problem/2579
import sys
n = int(input())
N = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = []
if n <=3:
    if n == 1:
        dp.append(N[0])
    elif n == 2:
        dp.append(sum(N))
    else:
        dp.append(N[0]) 
        dp.append(max(N[0]+N[1],N[1])) 
        dp.append(max(N[0]+N[2],N[1]+N[2]))
    print(dp[-1]) 
else:
    dp.append(N[0]) 
    dp.append(max(N[0]+N[1],N[1])) 
    dp.append(max(N[0]+N[2],N[1]+N[2])) 
    for i in range(3,n): 
        dp.append(max(dp[i-2] + N[i] , dp[i-3] + N[i] + N[i - 1]))
    print(dp[-1])

