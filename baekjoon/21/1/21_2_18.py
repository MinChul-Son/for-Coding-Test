# https://www.acmicpc.net/problem/1026
# n = int(input())
# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())), reverse=True)
# sum = 0
# for i in range(n):
#     sum += (a[i]*b[i])
# print(sum)


# https://www.acmicpc.net/problem/10815
# from bisect import bisect_left, bisect_right
# n = int(input())
# my_card = sorted(list(map(int, input().split())))
# m = int(input())
# input_card = list(map(int, input().split()))
# for i in input_card:
#     if bisect_left(my_card, i) == bisect_right(my_card, i):
#         print(0, end=" ")
#     else:
#         print(1, end=" ")


# https://www.acmicpc.net/problem/2217
# import sys
# n = int(input())
# rope = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
# weight_list = []
# for i in range(n):
#     weight_list.append(n*rope[i])
#     n -= 1
# print(max(weight_list))


# https://www.acmicpc.net/problem/1920
# from bisect import bisect_left, bisect_right
# n = int(input())
# N = sorted(list(map(int, input().split())))
# m = int(input())
# M = list(map(int, input().split()))
# for i in M:
#     if bisect_left(N, i) == bisect_right(N, i):
#         print(0)
#     else:
#         print(1)

# https://www.acmicpc.net/problem/10825



