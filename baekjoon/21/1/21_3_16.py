# https://www.acmicpc.net/problem/11048
# n, m = map(int, input().split())
# maze = [list(map(int, input().split())) for _ in range(n)]
# # max(maze[r-1][c], maze[r][c-1], maze[r-1][c-1])
# dp = [[0] * (m+1) for _ in range(n)]
# for i in range(1, m+1):
#     dp[0][i] += (maze[0][i-1] + dp[0][i-1])
# for i in range(1, n):
#     dp[i][1] += (maze[i][0] + dp[i-1][1])

# for i in range(1, n):
#     for j in range(2, m+1):
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j-1]
# print(dp[-1][-1])



