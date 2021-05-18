import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = [(a ** i) % 10 for i in range(1,5)]
    print(result[(b % 4) -1] if result[(b % 4) -1] != 0 else 10)

