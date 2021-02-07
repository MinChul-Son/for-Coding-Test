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
n = list(input())
n.sort(reverse=True)
print(n)
answer =  -1
max = 0
if n[-1] == '0':
    max = int("".join(n))
    if max % 3 == 0:
        answer = max
print(answer)
