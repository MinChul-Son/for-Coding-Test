# https://www.acmicpc.net/problem/2156
import sys
n = int(sys.stdin.readline())
wine_list = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0]
dp.append(wine_list[0])
if(n > 1):
    dp.append(wine_list[0] + wine_list[1])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+wine_list[i-1]+wine_list[i-2],dp[i-2]+wine_list[i-1]))
print(dp[-1])