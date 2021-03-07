# https://www.acmicpc.net/problem/5052
# import sys
# input = sys.stdin.readline
# a = [0] + list(input().strip())
# b = [0] + list(input().strip())
# len_a = len(a)
# len_b = len(b)
# dp = [[""] * len_b for i in range(len_a)]
# for i in range(1, len_a):
#     for j in range(1, len_b):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + a[i]
#         else:
#             if len(dp[i - 1][j]) > len(dp[i][j - 1]):
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 dp[i][j] = dp[i][j - 1]
# print(len(dp[len_a - 1][len_b - 1]))
# print(dp[len_a - 1][len_b - 1])


# https://www.acmicpc.net/problem/4358
# import sys
# tree_dic = dict()
# len_list = 0

# while True:
#     tree = sys.stdin.readline().strip()
#     if not tree:
#         break
#     len_list += 1
#     if tree in tree_dic:
#         tree_dic[tree] += 1
#     else:
#         tree_dic[tree] = 1
# sorted_tree = sorted(tree_dic.items())
# for i in sorted_tree:
#     print(i[0], end=" ")
#     print("%.4f" %((i[1]/len_list)*100))

