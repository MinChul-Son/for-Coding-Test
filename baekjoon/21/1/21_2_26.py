# https://www.acmicpc.net/problem/2156
# import sys
# n = int(sys.stdin.readline())
# wine_list = [int(sys.stdin.readline()) for _ in range(n)]
# dp = [0]
# dp.append(wine_list[0])
# if(n > 1):
#     dp.append(wine_list[0] + wine_list[1])
# for i in range(3, n+1):
#     dp.append(max(dp[i-1], dp[i-3]+wine_list[i-1]+wine_list[i-2],dp[i-2]+wine_list[i-1]))
# print(dp[-1])


# https://www.acmicpc.net/problem/1904
# n = int(input())
# a, b = 0, 1
# for i in range(n):
#     a, b = b%15746, (a + b)%15746
# print(b)


# https://www.acmicpc.net/problem/2293
# import sys
# n, k = map(int, sys.stdin.readline().split())
# coin_list = [int(sys.stdin.readline()) for _ in range(n)]
# dp = [0 for _ in range(k+1)] 
# dp[0] = 1
# for i in coin_list:
#     for j in range(1, k + 1):
#         if j - i >= 0:
#             dp[j] += dp[j - i]
# print(dp[k])


# https://www.acmicpc.net/problem/1748
answer = 0
for i in range(1, int(input())+1):
    answer += len(str(i))
print(answer)