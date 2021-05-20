# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
houses = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: houses.append((i, j))
        elif graph[i][j] == 2: chicken.append((i, j))

answer = 1000000
for combi in combinations(chicken, m):
    sum_distance = 0
    for house in houses:
        temp = 1000000
        for x, y in combi:
            temp = min(temp, abs(x-house[0]) + abs(y-house[1]))
        sum_distance += temp
    answer = min(answer, sum_distance)
print(answer)
