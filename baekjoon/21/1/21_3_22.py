# https://www.acmicpc.net/problem/1932
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j, p in enumerate(triangle[i]):
        if j != 0 and j != i:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    triangle[i][0] += triangle[i-1][0]
    triangle[i][-1] += triangle[i-1][-1]
print(max(triangle[-1]))