import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = [(a ** i) % 10 for i in range(1,5)]
    print(result[(b % 4) -1] if result[(b % 4) -1] != 0 else 10)

#----------------------------------------------------------------------
# https://www.acmicpc.net/problem/10871
import sys
input = sys.stdin.readline
n, x = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    if num < x:
        print(num, end=" ")

#-------------------------------------------------------------------------
# https://www.acmicpc.net/problem/2562
import sys
input = sys.stdin.readline
max_num = 0; max_idx = 0
for i in range(1, 10):
    input_num = int(input())
    if input_num > max_num:
        max_num = input_num
        max_idx = i
print(max_num)
print(max_idx)