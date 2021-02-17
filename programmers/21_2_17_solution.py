# https://www.acmicpc.net/problem/10953
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split(","))
#     print(a+b)

# https://www.acmicpc.net/problem/10808
# s = input()
# for i in range(97,123):
#     print(s.count(chr(i)), end=" ")

# https://www.acmicpc.net/problem/2743
# print(len(input()))

# https://www.acmicpc.net/problem/9251
# A = input(); B = input()
# lcs = [[0] * (len(A)+1) for _ in range(len(B)+1)]

# for i in range(1,len(B)+1) :
#     for j in range(1,len(A)+1) :
#         if B[i-1] == A[j-1] :
#             lcs[i][j] = lcs[i-1][j-1] + 1
#         else :
#             lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
# print(lcs[-1][-1])

# https://www.acmicpc.net/problem/1100
# import sys
# chess = [sys.stdin.readline().strip() for _ in range(8)]
# count = 0
# color = True
# for i in chess:
#     for j,p in enumerate(i):
#         if p == "F" and color:
#             count += 1
#         else:
#             pass
#         if j == 7:
#             pass
#         else:
#             if color:
#                 color = False
#             else:
#                 color = True
# print(count)



# https://www.acmicpc.net/problem/2902
# s = list(input().split("-"))
# for i in s:
#     print(i[0], end="")


# https://www.acmicpc.net/problem/1764
# import sys
# n, m = map(int, input().split())
# ears = set([sys.stdin.readline().strip() for _ in range(n)])
# eyes = set([sys.stdin.readline().strip() for _ in range(m)])
# ears_eyes = sorted(list(ears & eyes))
# print(len(ears_eyes))
# for i in ears_eyes:
#     print(i)

# https://www.acmicpc.net/problem/1032
# n = int(input())
# answer_1 = list(str(input()))

# for i in range(n-1):
#     answer_2 = list(str(input()))
#     for j in range(len(answer_1)):
#         if answer_1[j] != answer_2[j]:
#             answer_1[j] = '?'
# print(''.join(answer_1))
