# https://www.acmicpc.net/problem/1182
from itertools import combinations
n, s = map(int, input().split())
n_list = list(map(int, input().split()))
combi_list = []
count = 0
for i in range(1, n+1):
    combi_list.extend(list(combinations(n_list, i)))
for i in combi_list:
    if sum(i) == s:
        count += 1
print(count)