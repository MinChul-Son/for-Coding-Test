# https://www.acmicpc.net/problem/1495
import sys
input = sys.stdin.readline
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1
for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j] == 0:
            continue
        if j + volumes[i - 1] <= m:
            dp[i][j + volumes[i - 1]] = 1
        if j - volumes[i - 1] >= 0:
            dp[i][j - volumes[i - 1]] = 1

for i in range(m, -1, -1):
        if dp[-1][i] == 1:
            print(i)
            break
else:
    print(-1)

