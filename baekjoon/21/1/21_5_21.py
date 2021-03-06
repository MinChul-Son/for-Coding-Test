# https://www.acmicpc.net/problem/2167
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = a[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

#--------------------------------------------------------------------------
# https://www.acmicpc.net/problem/5565
import sys
input = sys.stdin.readline
total_price = int(input())
books_price = sum([int(input()) for _ in range(9)])
print(total_price-books_price)