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
print(max(dp))

#------------------------------------------------------------
# https://www.acmicpc.net/problem/15989
import sys
input = sys.stdin.readline
t = int(input())
dp = [1 for i in range(10001)] # 1로만 표현하는 것은 무조건 존재하므로 1부터 시작
nums = [int(input()) for _ in range(t)]

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]
for i in nums:
    print(dp[i])
