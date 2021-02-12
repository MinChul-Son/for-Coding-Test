# https://www.acmicpc.net/problem/2981
# import sys 
# import math 
# N = int(sys.stdin.readline()) 
# nums = [] 
# for i in range(N): 
#     nums.append(int(sys.stdin.readline())) 
#     nums.sort() 
#     mog = nums[-1] - nums[0] 
#     divisor = [mog] 
#     for i in range(2, int(math.sqrt(mog)) + 1): 
#         if mog % i == 0: 
#             divisor.append(i) 
#             divisor.append(mog//i) 
# divisor = list(set(divisor)) 
# divisor.sort() 
# for d in divisor: 
#     for i in range(N): 
#         if i == N - 1: 
#             print(d, end = " ") 
#         elif nums[i] % d != nums[i + 1] % d: 
#             break

# https://www.acmicpc.net/problem/5086
# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break
#     if n % m == 0:
#         print("multiple")
#     else:
#         if m % n == 0:
#             print("factor")
#         else:
#             print("neither")


# https://www.acmicpc.net/problem/3036
from math import gcd
n = int(input())
ring_list = list(map(int, input().split()))
for i in range(1,n):
    gcd_num = gcd(ring_list[0],ring_list[i])
    print(ring_list[0]//gcd_num, end="")
    print("/", end="")
    print(ring_list[i]//gcd_num)


