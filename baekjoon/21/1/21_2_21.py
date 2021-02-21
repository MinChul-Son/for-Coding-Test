# https://www.acmicpc.net/problem/11286
# import sys
# import heapq
# n = int(input())
# num_list =[int(sys.stdin.readline()) for _ in range(n)]
# heap = []
# for i in num_list:
#     if i != 0:
#         heapq.heappush(heap, (abs(i), i))
#     else:
#         if not heap:
#             print(0)
#         else:
#             print(heapq.heappop(heap)[1])



# https://www.acmicpc.net/problem/2493
# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=list(map(int,input().split()))
# stack=[]
# ans=[]
# for i in range(0,n):
#     while True:
#         if not stack:
#             stack.append((i,arr[i]))
#             ans.append(0)
#             break
#         if stack[-1][1]>=arr[i]:
#             ans.append(stack[-1][0]+1)
#             stack.append((i,arr[i]))
#             break
#         else:
#             stack.pop()
# print(*ans)




# https://www.acmicpc.net/problem/2357
# import sys
# n, m = map(int, input().split())
# N_list = [int(sys.stdin.readline()) for _ in range(n)]
# M_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# for i,j in M_list:
#     max_num = N_list[i-1]
#     min_num = N_list[i-1]
#     for k in range(i-1, j):
#         if N_list[k] > max_num:
#             max_num = N_list[k]
#         if N_list[k] < min_num:
#             min_num = N_list[k]
#     print(min_num, max_num)
## 실패



# https://www.acmicpc.net/problem/1918
# import sys
# from math import sqrt
# input=sys.stdin.readline

# d={'*':2,'/':2,'+':1,'-':1,'(':0,')':0}
# q=[]
# s=input().strip()
# for x in s:
#     # 알파벳 출력
#     if x not in d:
#         print(x,end='')
#     #왼쪽 괄호 
#     elif x=='(':
#         q.append(x)
#     # 오른쪽 괄호시 왼쪽 괄호 나올때까지 중간 연산자 출력한다 
#     elif x==')':
#         while q:
#             cur=q.pop()
#             if cur=='(': break
#             print(cur,end='')
#     else:
#         # 우선순위가 더 낮다면 이전에 우선순위 높은 연산자를 출력한다 
#         while q and q[-1]!='(' and d[x]<=d[q[-1]]:
#             print(q.pop(),end='')
#         q.append(x)

# # 나머지 연산자를 출력한다 
# while q:
#     print(q.pop(),end='')
        










