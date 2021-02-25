# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
alpha_list = sorted(list(sys.stdin.readline().split()))
combi_list = list(combinations(alpha_list, l))
vowels = ['a', 'e', 'i', 'o', 'u']
for i in combi_list:
    count = 0
    for j in i:
        if j in vowels:
            count += 1
    if (count >= 1) and (count <= l-2):
        print(''.join(i))
