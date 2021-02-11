# https://www.acmicpc.net/problem/10872
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)


# n = int(input())
# print(factorial(n))


# https://www.acmicpc.net/problem/10870
# def fibonacci(num):
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)
# n = int(input())
# print(fibonacci(n))


# https://www.acmicpc.net/problem/10819
# from itertools import permutations
# n = int(input())
# num_list = list(map(int, input().split()))
# num_list = list(permutations(num_list,n))
# max = 0
# for i in num_list:
#     temp = 0
#     for j in range(0,n-1):
#         temp += abs(i[j]-i[j+1])
#     if temp > max:
#         max = temp
# print(max)

# https://www.acmicpc.net/problem/11053

# n= int(input()) 
# nl = list(map(int,input().split())) 
# arr = [0]*1001 
# for i in nl: 
#     arr[i] = max(arr[:i]) + 1
# print(max(arr))

# https://www.acmicpc.net/problem/11057
# n = int(input())
# s = [[0] * 10 for i in range(1001)]
# for i in range(10):
#     s[1][i] = 1
# for i in range(2, 1001):
#     for j in range(10):
#         for k in range(j + 1):
#             s[i][j] += s[i - 1][k]
# print(sum(s[n]) % 10007)

