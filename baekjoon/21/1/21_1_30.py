# https://www.acmicpc.net/problem/11047
# import sys
# n, k = map(int,input().split())
# N = list(map(int,(sys.stdin.readline().strip() for _ in range(n))))
# count = 0
# N.reverse()
# while k:
#     for i in N:
#         if (k // i) > 0 :
#             count += (k // i)
#             k -= (i * (k // i))
# print(count)

# https://www.acmicpc.net/problem/1931
# import sys
# n = int(input())
# N = list(tuple(map(int,(sys.stdin.readline().split()))) for _ in range(n))
# N= sorted(N, key=lambda x : (x[1],x[0]))
# count = 0
# finish = 0
# for i,j in N:
#     if i >= finish:
#         count += 1
#         finish = j
# print(count)



