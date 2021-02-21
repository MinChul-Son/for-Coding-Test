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








