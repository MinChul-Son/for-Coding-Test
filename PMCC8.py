import sys
N = int(sys.stdin.readline())
tree = [0 for _ in range(N+1)]
count = 0
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u] = v

print(tree)