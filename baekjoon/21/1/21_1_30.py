# https://www.acmicpc.net/problem/11047
# import sys
# n, k = map(int,input().split())
# N = list(map(int,(sys.stdin.readline().strip() for _ in range(n))))
# count = 0
# N.reverse()
# while k:
#     for i in N:
#         if (k // i) > 0 :
#             count += (k // i)
#             k -= (i * (k // i))
# print(count)

# https://www.acmicpc.net/problem/1931
# import sys
# n = int(input())
# N = list(tuple(map(int,(sys.stdin.readline().split()))) for _ in range(n))
# N= sorted(N, key=lambda x : (x[1],x[0]))
# count = 0
# finish = 0
# for i,j in N:
#     if i >= finish:
#         count += 1
#         finish = j
# print(count)



# https://www.acmicpc.net/problem/11399
# import sys
# n = int(input())
# N = list(map(int,input().split()))
# N.sort()
# answer = 0
# time_sum = 0
# for i in N:
#     time_sum += i
#     answer += time_sum
# print(answer)

# https://www.acmicpc.net/problem/1541
# n = input().split('-')
# print(n)
# answer = 0
# for i in n[0].split('+'):
#     answer += int(i)
# for i in n[1:]:
#     for j in i.split('+'):
#         answer -= int(j)
# print(answer)

# https://www.acmicpc.net/problem/13305
# import sys
# n = int(input())
# order = list(sys.stdin.readline().split() for _ in range(n))
# stack = []
# for i in order:
#     if i[0] == 'push':
#         stack.append(int(i[1]))
#     elif i[0] == 'pop':
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif i[0] == 'size':
#         print(len(stack))
#     elif i[0] == 'empty':
#         if stack:
#             print(0)
#         else:
#             print(1)
#     else:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)


# https://www.acmicpc.net/problem/10773
# import sys
# n = int(input())
# N = list(sys.stdin.readline().strip() for _ in range(n))
# stack = []
# for i in N:
#     if i == '0':
#         stack.pop()
#     else:
#         stack.append(int(i))
# print(sum(stack))

# https://www.acmicpc.net/problem/9012
# import sys
# n = int(input())
# N = list(sys.stdin.readline().strip() for _ in range(n))
# for i in N:
#     count = 0
#     if i[0] == ')' or i[-1] == '(':
#         print('NO')
#     else:
#         for j in i:
#             if j =='(':
#                 count += 1
#             else:
#                 count -= 1
#             if count < 0:
#                 print('NO')
#                 break
#         else:
#             if count == 0:
#                 print('YES')   
#             else:
#                 print('NO')
