# https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline

n = int(input())
rest = n%5

if n == 1 or n == 3:
    print(-1)
elif rest % 2 == 0:
    print(n // 5 + rest // 2)
else:
    print((n // 5) -1 + (rest + 5) // 2)