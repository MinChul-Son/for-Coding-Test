# https://www.acmicpc.net/problem/7662
import sys
import heapq
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    count = 0
    for _ in range(k):
        cmd = list(input().split())
        if cmd[0] == 'I':
            count += 1
            heapq.heappush(min_heap, int(cmd[1]))
            heapq.heappush(max_heap, (-int(cmd[1]), int(cmd[1])))
        else:
            if count == 0:
                min_heap = []
                max_heap = []
                continue
            count -= 1
            if cmd[1] == '-1':
                heapq.heappop(min_heap)
            else:
                heapq.heappop(max_heap)
    max_heap = [i[1] for i in max_heap]
    intersection_list = list(set(min_heap) & set(max_heap))
    if intersection_list:
        print(max(intersection_list), min(intersection_list))
    else:
        print("EMPTY")
#-------------------------------------------------------------------------
import heapq
def sync(arr):
    while arr and id[arr[0][1]] == 0:
        heapq.heappop(arr)

T = int(input())
for test_case in range(T):
    max_arr = []
    min_arr = []
    id = [0] * 1000000
    K = int(input())
    count = 0
    for i in range(K):
        S, num = input().split()

        if S == "I":
            heapq.heappush(max_arr, (-1 * int(num), i))
            heapq.heappush(min_arr, (int(num),i))
            id[i] = 1
            
        else:

            if num == "1":
                sync(max_arr)
                if max_arr:
                    id[max_arr[0][1]] = 0
                    heapq.heappop(max_arr)

            elif num == "-1":
                sync(min_arr)
                if min_arr:
                    id[min_arr[0][1]] = 0
                    heapq.heappop(min_arr)

    sync(max_arr)
    sync(min_arr)

    if len(max_arr) == 0:
        print("EMPTY")
    else:
        print(-1 * max_arr[0][0], end =" ")
        print(min_arr[0][0])