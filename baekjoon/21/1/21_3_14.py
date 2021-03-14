# https://www.acmicpc.net/problem/7576
# from collections import deque
# m, n = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# already_ripen = False
# isall_ripen = False
# for i in graph:
#     if 0 in i:
#         break
# else:
#     already_ripen = True

# if already_ripen:
#     print(0)
# else:
#     queue = deque()
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 queue.append([i, j])
#     move_x = [1, -1, 0, 0]
#     move_y = [0, 0, -1, 1]
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             x = a + move_x[i]
#             y = b + move_y[i]
#             if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
#                 queue.append([x, y])
#                 graph[x][y] = graph[a][b] + 1
#     for i in graph:
#         if 0 in i:
#             break
#     else:
#         isall_ripen = True
#     if not isall_ripen:
#         print(-1)
#     else:
#         result = 0
#         for i in graph:
#             for j in i:
#                 if j > result:
#                     result = j
#         print(result-1)



# https://www.acmicpc.net/problem/14490
# from math import gcd
# n, m = map(int, input().split(':'))
# while True:
#     gcd_num = gcd(n, m)
#     if gcd_num == 1:
#         break
#     n //= gcd_num
#     m //= gcd_num
# print(str(n) + ":" + str(m))



# https://www.acmicpc.net/problem/16916
# import sys                              ## 시간 초과
# s = sys.stdin.readline().strip()
# p = sys.stdin.readline().strip()
# for i in range(len(s)-len(p) + 1):
#     if s[i:i+len(p)] == p:
#         print(1)
#         break
# else:
#     print(0)

import sys
s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
def getPartialMatch(N):
    m = len(N)
    pi = [0] * m
    # KMP로 N에서 N을 찾는다 (begin은 1부터)
    begin = 1
    matched = 0
    # 비교할 문자가 N의 끝에 도달할 때까지 부분 일치를 모두 기록
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

def kmpSearch(H, N):
    n = len(H)
    m = len(N)
    # 결과값 리스트
    ret = []
    # pi[i]는 N[~i]의 접두사도 되고 접미사는 되는 문자열의 최대 길이
    pi = getPartialMatch(N)
    begin = 0
    matched = 0
    while begin <= n - m:
    # 글자가 일치한다면
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
        # m글자가 모두 일치한다면
            if matched == m:
                ret.append(begin)
        else:
        # matched가 0인 경우 다음 칸에서 시작
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return ret
if kmpSearch(s, p):
    print(1)
else:
    print(0)

