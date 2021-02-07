# https://www.acmicpc.net/problem/2609
# from math import gcd
# n,m = map(int, input().split())
# print(gcd(n,m))
# print((n*m)//gcd(n,m))

# https://www.acmicpc.net/problem/1059
# l = int(input())
# s = list(map(int,input().split()))
# n = int(input())
# s.sort()
# answer = 0
# idx = 0
# check = True
# if n in s:
#     print(0)
# else:
#     for i in range(l-1):
#         if s[i] < n and n < s[i+1]:
#             idx = i
#             check = False
#             break
#     else:
#         for i in range(1,s[idx]):
#             for j in range(i+1,s[idx]):
#                 if i <= n and j >= n:
#                     answer += 1
#         print(answer)
#     if not check:
#         for i in range(s[idx]+1,s[idx+1]):
#             for j in range(i+1,s[idx+1]):
#                 if i <= n and j >= n:
#                     answer += 1
#         print(answer)


# https://www.acmicpc.net/problem/1063
# import sys
# k, s, n = input().split()
# move = [sys.stdin.readline().strip() for _ in range(int(n))]
# row = ['A','B','C','D','E','F','G','H']
# column = ['1','2','3','4','5','6','7','8']
# king_idx = []
# stone_idx = []
# for i,p in enumerate(row):
#     if p == k[0]:
#         king_idx.append(i)
#         break
# for i,p in enumerate(column):
#     if p == k[1]:
#         king_idx.append(i)
#         break
# for i,p in enumerate(row):
#     if p == s[0]:
#         stone_idx.append(i)
#         break
# for i,p in enumerate(column):
#     if p == s[1]:
#         stone_idx.append(i)
#         break

# # 명령 수행
# for i in move:
#     if i == 'R':
#         if king_idx[0] == 7:
#             continue
#         king_idx[0] += 1
#         if king_idx == stone_idx:
#             if stone_idx[0] == 7:
#                 king_idx[0] -= 1
#                 continue
#             stone_idx[0] += 1
#     elif i == 'L':
#         if king_idx[0] == 0:
#             continue
#         king_idx[0] -= 1
#         if king_idx == stone_idx:
#             if stone_idx[0] == 0:
#                 king_idx[0] += 1
#                 continue
#             stone_idx[0] -= 1
#     elif i == 'B':
#         if king_idx[1] == 0:
#             continue
#         king_idx[1] -= 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 0:
#                 king_idx[1] += 1
#                 continue
#             stone_idx[1] -= 1
#     elif i == 'T':
#         if king_idx[1] == 7:
#             continue
#         king_idx[1] += 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 7:
#                 king_idx[1] -= 1
#                 continue
#             stone_idx[1] += 1
#     elif i == 'RT':
#         if king_idx[1] == 7 or king_idx[0] == 7:
#             continue
#         king_idx[0] += 1
#         king_idx[1] += 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 7 or stone_idx[0] == 7:
#                 king_idx[0] -= 1
#                 king_idx[1] -= 1
#                 continue
#             stone_idx[0] += 1
#             stone_idx[1] += 1
#     elif i == 'LT':
#         if king_idx[1] == 7 or king_idx[0] == 0:
#             continue
#         king_idx[0] -= 1
#         king_idx[1] += 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 7 or stone_idx[0] == 0:
#                 king_idx[0] += 1
#                 king_idx[1] -= 1
#                 continue
#             stone_idx[0] -= 1
#             stone_idx[1] += 1
#     elif i == 'RB':
#         if king_idx[1] == 0 or king_idx[0] == 7:
#             continue
#         king_idx[0] += 1
#         king_idx[1] -= 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 0 or stone_idx[0] == 7:
#                 king_idx[0] -= 1
#                 king_idx[1] += 1
#                 continue
#             stone_idx[0] += 1
#             stone_idx[1] -= 1
#     elif i == 'LB':
#         if king_idx[1] == 0 or king_idx[0] == 0:
#             continue
#         king_idx[0] -= 1
#         king_idx[1] -= 1
#         if king_idx == stone_idx:
#             if stone_idx[1] == 0 or stone_idx[0] == 0:
#                 king_idx[0] += 1
#                 king_idx[1] += 1
#                 continue
#             stone_idx[0] -= 1
#             stone_idx[1] -= 1
# print(row[king_idx[0]]+column[king_idx[1]])
# print(row[stone_idx[0]]+column[stone_idx[1]])


# https://www.acmicpc.net/problem/1934
# from math import gcd
# n = int(input())
# for _ in range(n):
#     n, m = map(int,input().split())
#     print((n*m)//gcd(n,m))

# https://www.acmicpc.net/problem/1476
# e, s, m = map(int,input().split())
# E, S, M, answer = 1, 1, 1, 1
# while True:
#     if e == E and s == S and m == M:
#         break
#     E += 1
#     S += 1
#     M += 1
#     answer += 1
#     if E >= 16:
#         E -= 15
#     if S >= 29:
#         S -= 28
#     if M >= 20:
#         M -= 19
# print(answer)

# https://www.acmicpc.net/problem/1475
n = list(map(int,list(input())))
count_num = [0 for _ in range(10)]
for i in n:
    if i == 6 or i == 9:
        if count_num[6] == count_num[9]:
            count_num[6] += 1
        else:
            count_num[9] += 1
    else:
        count_num[i] += 1
print(max(count_num))
