# https://www.acmicpc.net/problem/1715
import sys
import heapq
input = sys.stdin.readline
n = int(input())
queue = []
for _ in range(n):
    heapq.heappush(queue, int(input()))
answer = 0
while len(queue) > 1:
    x = heapq.heappop(queue) ; y = heapq.heappop(queue)
    answer += (x+y)
    heapq.heappush(queue, x+y)
print(answer)


