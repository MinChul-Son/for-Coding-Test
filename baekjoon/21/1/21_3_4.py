# https://www.acmicpc.net/problem/11441
# import sys
# n = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# cum = [num_list[0]]
# for i in range(1, n):
#     cum.append(cum[-1]+num_list[i])
# for i, j in m_list:
#     if i == 1:
#         print(cum[j-1])
#     else:
#         print(cum[j-1]-cum[i-2])


# https://www.acmicpc.net/problem/13241
# from math import gcd
# a, b = map(int, input().split())
# print(a*b//(gcd(a, b)))



# https://www.acmicpc.net/problem/1431
import sys
n = int(sys.stdin.readline())
guitar_list = []
for _ in range(n):
    serial_number = sys.stdin.readline().strip()
    number_sum = 0
    for i in serial_number:
        if i.isdigit():
            number_sum += int(i)
    guitar_list.append([serial_number, number_sum])
guitar_list = sorted(guitar_list, key=lambda x: (len(x[0]), x[1], x[0]))
for i in guitar_list:
    print(i[0])
