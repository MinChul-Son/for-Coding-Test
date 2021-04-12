# https://www.acmicpc.net/problem/1351
from collections import defaultdict
import sys
def dp(n):
    if data[n] != 0:
        return data[n]
    data[n] = dp(n // p) + dp(n // q)
    return data[n]
input = sys.stdin.readline
n, p, q = map(int, input().split())
data = defaultdict(int)
data[0] = 1
print(dp(n))