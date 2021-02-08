# https://www.acmicpc.net/problem/1094
# x = int(input())
# arr = [64]; temp =64; cnt = 0
# for i in range(6):
#     temp//=2
#     arr.append(temp)
# if x in arr :
#     print(1)
# else :
#     for q in arr :
#         if x >= q :
#             x -= q
#             cnt +=1
#     print(cnt)

# https://www.acmicpc.net/problem/11004
# n ,k = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# print(A[k-1])

# https://www.acmicpc.net/problem/10610
# n = list(input())
# n.sort(reverse=True)
# answer =  -1
# max = 0
# if n[-1] == '0':
#     max = int("".join(n))
#     if max % 3 == 0:
#         answer = max
# print(answer)

# https://www.acmicpc.net/problem/10867
# n = int(input())
# N = list(map(int,set(input().split())))
# for i in sorted(N):
#     print(i, end=" ")

# https://www.acmicpc.net/problem/1978
# n = int(input())
# N = list(map(int, input().split()))
# answer = 0
# for i in N:
#     count = 0
#     if i != 1:
#         for j in range(1,i+1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             answer += 1
# print(answer)

# https://www.acmicpc.net/problem/2581
# m = int(input())
# n = int(input())
# temp_list = []
# for i in range(m, n+1):
#     count = 0
#     if i != 1:
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             temp_list.append(i)
# if temp_list:
#     print(sum(temp_list))
#     print(min(temp_list))
# else:
#     print(-1)



