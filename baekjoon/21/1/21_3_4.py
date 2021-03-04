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


