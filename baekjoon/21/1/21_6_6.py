# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline
n = int(input())
cost_list = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
max_cost = 0
for i in range(n):
    max_cost = max(max_cost, dp[i])
    if i + cost_list[i][0] > n:
        continue
    dp[i+cost_list[i][0]] = max(max_cost+cost_list[i][1], dp[i+ cost_list[i][0]])
    print(dp)
print(max(dp))