# https://www.acmicpc.net/problem/1759
# import sys
# from itertools import combinations
# l, c = map(int, sys.stdin.readline().split())
# alpha_list = sorted(list(sys.stdin.readline().split()))
# combi_list = list(combinations(alpha_list, l))
# vowels = ['a', 'e', 'i', 'o', 'u']
# for i in combi_list:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1
#     if (count >= 1) and (count <= l-2):
#         print(''.join(i))


# https://www.acmicpc.net/problem/1107
# import sys
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# trouble_btn = set(sys.stdin.readline().split())
# btn = {str(i) for i in range(10)}
# btn = btn - trouble_btn
# result = abs(n-100)
# for i in range(1000001):
#     for part_num in str(i):
#         if (part_num not in btn):
#             break
#     else:
#         result = min(result, abs(n - i) + len(str(i)))

# print(result)



# https://www.acmicpc.net/problem/20920
import sys
n, m = map(int, input().split())
note = dict()
for _ in range(n):
    s = sys.stdin.readline().strip()
    if len(s) >= m:
        if s in note:
            note[s] += 1
        else:
            note[s] = 1
note = sorted(note.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
for i in note:
    print(i[0])