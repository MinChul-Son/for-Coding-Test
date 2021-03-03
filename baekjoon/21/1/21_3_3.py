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
import sys
document = sys.stdin.readline().strip()
search_word = sys.stdin.readline().strip()
count = 0
while True:
    if search_word in document:
        count += 1
        document = document.replace(search_word, "", 1)
    else:
        break
print(count)
