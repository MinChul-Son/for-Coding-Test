# https://www.acmicpc.net/problem/1026
# n = int(input())
# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())), reverse=True)
# sum = 0
# for i in range(n):
#     sum += (a[i]*b[i])
# print(sum)


# https://www.acmicpc.net/problem/10815
from bisect import bisect_left, bisect_right
n = int(input())
my_card = sorted(list(map(int, input().split())))
m = int(input())
input_card = list(map(int, input().split()))
for i in input_card:
    if bisect_left(my_card, i) == bisect_right(my_card, i):
        print(0, end=" ")
    else:
        print(1, end=" ")

