# https://www.acmicpc.net/problem/2908
a, b = input().split()
a = list(a); b = list(b); a.reverse(); b.reverse(); a = int("".join(a)); b = int("".join(b))
if a > b:
    print(a)
else:
    print(b)