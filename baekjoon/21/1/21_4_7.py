# https://www.acmicpc.net/problem/11000
# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())
# lectures = [list(map(int, input().split())) for _ in range(n)]
# lectures = sorted(lectures, key=lambda x: (x[0], x[1]))
# count = 1
# queue = []
# heapq.heappush(queue, lectures[0][1])
# for i in range(1, n):
#     if lectures[i][0] >= queue[0]:
#         heapq.heappop(queue)
#         heapq.heappush(queue, lectures[i][1])
#     else:
#         count += 1
#         heapq.heappush(queue, lectures[i][1])
# print(count)


# https://www.acmicpc.net/problem/2812
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# num = list(input().strip())
# stack, temp = [], k
# for i in range(n):
#     while temp > 0 and stack and stack[-1] < num[i]:
#         del stack[-1]
#         temp -= 1
#     stack.append(num[i])
# print(''.join(stack[:n - k]))


# https://www.acmicpc.net/problem/2109
import sys
import heapq
input = sys.stdin.readline
n = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], -x[0]))
queue = []
for i in lectures:
    heapq.heappush(queue, i[0])
    if len(queue) > i[1]:
        heapq.heappop(queue)
print(sum(queue))




