# https://www.acmicpc.net/problem/10844
# n = int(input())
# dp = [[0 for i in range(10)] for j in range(101)]
# for i in range(1, 10):
#     dp[1][i] = 1
# for i in range(2, n + 1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i - 1][1]
#         elif j == 9:
#             dp[i][j] = dp[i - 1][8]
#         else:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
# print(sum(dp[n]) % 1000000000)



# https://www.acmicpc.net/problem/1120
# a, b = input().split()
# b = list(b)
# len_a = len(a)
# max_cnt = 0
# while len_a <= len(b):
#     cnt = 0
#     for i in range(len_a):
#         if a[i] == b[i]:
#             cnt += 1
#     max_cnt = max(max_cnt, cnt)
#     print(a,b)
#     del b[0]
# print(len_a - max_cnt)

# https://www.acmicpc.net/problem/17413
# from collections import deque
# s = deque(input())
# answer = ''
# queue = deque()
# while s:
#     temp = s.popleft()
#     if temp == "<":
#         answer += "".join(reversed(queue))
#         queue.clear()
#         queue.append(temp)
#         while True:
#             find_close = s.popleft()
#             if find_close == ">":
#                 queue.append(find_close)
#                 break
#             queue.append(find_close)
#         answer += "".join(queue)
#         queue.clear()
#     elif temp == " ":
#         answer += ("".join(reversed(queue)) + temp)
#         queue.clear()
#     else:
#         queue.append(temp)
# answer += ("".join(reversed(queue)))
# print(answer)


# https://www.acmicpc.net/problem/1305
# L = int(input())
# current_s = input()
# s_len = len(current_s)

# p_table = [0 for _ in range(s_len)]
# j = 0
# for i in range(1, s_len):
#     while j > 0 and current_s[i] != current_s[j]:
#         j = p_table[j-1]
#     if current_s[i] ==current_s[j]:
#         j += 1
#         p_table[i] = j
# p_len = s_len - p_table[s_len - 1]
# print(p_len)



