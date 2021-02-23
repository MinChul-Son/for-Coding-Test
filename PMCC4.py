import sys
from itertools import combinations
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
combi_list = list(combinations(N_list,2))
combi_list.sort(key=lambda x: sum(x))
comb_count = len(combi_list)
if comb_count % 2 == 0:
    print(sum(combi_list[(comb_count//2) -1]))
else:
    print(sum(combi_list[(comb_count//2)]))
