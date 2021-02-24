# https://www.acmicpc.net/problem/1182
# from itertools import combinations
# n, s = map(int, input().split())
# n_list = list(map(int, input().split()))
# combi_list = []
# count = 0
# for i in range(1, n+1):
#     combi_list.extend(list(combinations(n_list, i)))
# for i in combi_list:
#     if sum(i) == s:
#         count += 1
# print(count)



# https://www.acmicpc.net/problem/10974
# from itertools import permutations
# n = int(input())
# n_list = [i for i in range(1, n+1)]
# n_list = sorted(list(permutations(n_list, n)))
# for i in n_list:
#     print(*i)



# https://www.acmicpc.net/problem/5525
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# M = int(input().rstrip())
# S = input().rstrip()

# answer = 0
# count = 0
# i = 1

# while i < M - 1:
#     if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
#         count += 1
#         if count == N:
#             count -= 1
#             answer += 1
#         i += 1
#     else:
#         count = 0
#     i += 1

# print(answer)



# https://www.acmicpc.net/problem/9461
# wh = [0 for i in range(101)]
# wh[1] = 1
# wh[2] = 1
# wh[3] = 1
# for i in range(0, 98):
#     wh[i + 3] = wh[i] + wh[i + 1]
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     print(wh[n])



# https://www.acmicpc.net/problem/11723
# import sys
# s = set()
# m = int(sys.stdin.readline())
# for _ in range(m):
#     order = list(sys.stdin.readline().split())
#     if order[0] == 'add':
#         s.add(order[1])
#     elif order[0] == 'remove':
#         s.discard(order[1])
#     elif order[0] == 'check':
#         if order[1] in s:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'toggle':
#         if order[1] in s:
#             s.discard(order[1])
#         else:
#             s.add(order[1])
#     elif order[0] == 'all':
#         s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
#     elif order[0] == 'empty':
#         s = set()
        