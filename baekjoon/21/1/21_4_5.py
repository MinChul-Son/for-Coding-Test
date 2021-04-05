# https://www.acmicpc.net/problem/1715
# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())
# queue = []
# for _ in range(n):
#     heapq.heappush(queue, int(input()))
# answer = 0
# while len(queue) > 1:
#     x = heapq.heappop(queue) ; y = heapq.heappop(queue)
#     answer += (x+y)
#     heapq.heappush(queue, x+y)
# print(answer)


# https://www.acmicpc.net/problem/2075
import sys
import heapq
input = sys.stdin.readline
n = int(input())
queue = list(map(int, input().split()))
heapq.heapify(queue)
for _ in range(n-1):
    for i in list(map(int, input().split())):
        if i > queue[0]:
            heapq.heappop(queue)
            heapq.heappush(queue, i)
print(queue[0])




