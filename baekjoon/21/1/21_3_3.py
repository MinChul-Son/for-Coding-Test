# https://www.acmicpc.net/problem/1051
# n, m = map(int, input().split())
# num_list = [list(map(int, input())) for _ in range(n)]
# answer = 0
# for i in range(n):
#     for j in range(m):
#         for k in range(n if n < m else m):
#             if i+k < n and j+k < m:
#                 if num_list[i][j] == num_list[i][j+k] == num_list[i+k][j] == num_list[i+k][j+k]:
#                     if answer < k:
#                         answer = k
# print((answer+1)**2)



# https://www.acmicpc.net/problem/1543
# import sys
# document = sys.stdin.readline().strip()
# search_word = sys.stdin.readline().strip()
# index = 0
# cnt = 0
# while len(document) - index >= len(search_word):
#     if document[index:index+len(search_word)] == search_word:
#         cnt += 1
#         index += len(search_word)
#     else:
#         index += 1
# print(cnt)


# https://www.acmicpc.net/problem/2110
# N = int(input())
# budget = list(map(int, input().split()))
# M = int(input())

# start, end = 0, max(budget)
# total_budget = 0

# if M >= sum(budget):
# 	print(max(budget))
# else:
#     while start <= end:
#         mid = (start+end) // 2

#         total_budget = 0
#         for i in budget:
#             total_budget += min(mid, i)

#         if total_budget > M:
#             end = mid - 1
#         else:
#             start = mid + 1
#     print(end)



# https://www.acmicpc.net/problem/10972
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
x = 0
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()
print(-1)
    





