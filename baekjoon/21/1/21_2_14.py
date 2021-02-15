# https://www.acmicpc.net/problem/2004
# from math import factorial
# n, m = map(int, input().split())
# temp = str(factorial(n) // (factorial(m) * factorial(n - m)))
# start = -1
# count = 0
# while True:
#     if temp[start] == '0':
#         count += 1
#         start -= 1
#     else:
#         break
# print(count)


# def countNum(N, num): 
#     count = 0 
#     divNum = num 
#     while( N >= divNum): 
#         count = count + (N // divNum) 
#         divNum = divNum * num 
#     return count
# m, n = map(int, input().split())
# print(min(countNum(m, 5) - countNum(n, 5) - countNum(m-n, 5), countNum(m, 2) - countNum(n, 2) - countNum(m-n, 2)))



