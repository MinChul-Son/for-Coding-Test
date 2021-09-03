# https://www.acmicpc.net/problem/1269
import sys
input = sys.stdin.readline

A_len, B_len = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
answer = len(A-B) + len(B-A)
print(answer)