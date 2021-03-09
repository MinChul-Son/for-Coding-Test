# https://www.acmicpc.net/problem/1011
# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)


# https://www.acmicpc.net/problem/9020
from itertools import combinations
t = int(input())
# n이하의 소수 구하여 조합하기
primes = [0 for i in range(10001)]
primes[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        primes[j] = 1
for _ in range(t):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if primes[a - j] == 0 and primes[j] == 0:
            print(j, a - j)
            break
