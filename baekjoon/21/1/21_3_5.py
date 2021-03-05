# https://www.acmicpc.net/problem/2644
import sys
n = int(sys.stdin.readline())
cal_num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
print(tree)