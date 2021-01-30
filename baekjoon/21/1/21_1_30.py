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


# https://www.acmicpc.net/problem/4949
# while True:
#     string = input()
#     stack = []
#     temp = True
#     if string == '.':
#         break
#     for i in string:
#         if i == '(' or i == '[':
#             stack.append(i)
#         elif i == ')':
#             if not stack or stack[-1] == '[':
#                 temp = False
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#         elif i == ']':
#             if not stack or stack[-1] == '(':
#                 temp = False
#                 break
#             elif stack[-1] == '[':
#                 stack.pop() 
#     if temp == True and not stack:
#         print('yes')
#     else:
#         print('no')
        

# https://www.acmicpc.net/problem/1874
# import sys
# n = int(input())
# N = list(sys.stdin.readline().strip() for _ in range(n))
# stack = []
# answer = []
# count = 1
# possible = True
# for i in N:
#     while count <= int(i):
#         stack.append(count)
#         answer.append('+')
#         count += 1
#     if stack.pop() == int(i):
#         answer.append('-')
#     else:
#         possible = False
# if possible:
#     print('\n'.join(answer))
# else:
#     print('NO')


# https://www.acmicpc.net/problem/17298
# n = int(input())
# N = list(map(int,input().split()))
# answer = []
# for i,p in enumerate(N):
#     stack = []
#     for j in range(i,n):
#         if p<N[j]:
#             print(N[j], end=" ")
#             break
#     else:
#         print(-1,end=" ")


num = int(input())
a = list(map(int, input().split(" ")))
result = ["-1" for _ in range(num)]
stack = []
stack.append(0)
i = 1
for i in range(num):
    while stack and a[stack[-1]] < a[i]:
        result[stack[-1]] = str(a[i])
        stack.pop()

    stack.append(i)
    i += 1

print(" ".join(result))

