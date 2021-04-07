# https://www.acmicpc.net/problem/11000
import sys
import heapq
input = sys.stdin.readline
n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures = sorted(lectures, key=lambda x: (x[0], x[1]))
count = 1
queue = []
heapq.heappush(queue, lectures[0][1])
for i in range(1, n):
    if lectures[i][0] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, lectures[i][1])
    else:
        count += 1
        heapq.heappush(queue, lectures[i][1])
print(count)