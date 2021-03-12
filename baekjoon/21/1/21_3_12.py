# https://www.acmicpc.net/problem/1991

# def preorder(node):
#     if node == '.':
#         return
#     print(node, end="")
#     preorder(tree[node][0]) #왼쪽 서브트리
#     preorder(tree[node][1]) #오른쪽 서브트리

# def inorder(node):
#     if node == '.':
#         return
#     inorder(tree[node][0])
#     print(node, end="")
#     inorder(tree[node][1])

# def postorder(node):
#     if node == '.':
#         return
#     postorder(tree[node][0])
#     postorder(tree[node][1])
#     print(node, end="")

# n = int(input()) 
# tree = {}
# for _ in range(n): 
#     root, left, right = input().split() 
#     tree[root] = (left, right)
# preorder('A') 
# print() 
# inorder('A') 
# print() 
# postorder('A')


# https://www.acmicpc.net/problem/4963
# import sys
# sys.setrecursionlimit(10**6)

# def dfs(x, y):
#     if x <= -1 or x >= h or y <= -1 or y >= w:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 2
#         for i in range(8):
#             a = x + move_x[i]
#             b = y + move_y[i]      
#             dfs(a, b)   
#         return True
#     return False


# while True:
#     w, h = map(int, input().split())
#     if w == h == 0:
#         break

#     graph = [list(map(int, input().split())) for _ in range(h)]
#     move_x = [1, -1, 0, 0, 1, -1, -1, 1]
#     move_y = [0, 0, -1, 1, 1, 1, -1, -1]
#     result = 0
#     for i in range(h):
#         for j in range(w):
#             if dfs(i,j) == True:
#                 result += 1
#     print(result)


# https://www.acmicpc.net/problem/2003
# import sys
# n, m = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))
# answer = 0
# for i in range(n):
#     temp_sum = 0
#     for j in range(i, n):
#         temp_sum += nums[j]
#         if temp_sum == m:
#             answer += 1
#             break
#         if temp_sum > m:
#             break
# print(answer)

# 두 포인터 사용
import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
start = 0
end = 1
count = 0
sum = nums[start]
if sum == m:
    count += 1
while not (start == end == n):
    if sum < m and end < n:
        sum += nums[end]
        end += 1
    else:
        sum -= nums[start]
        start += 1

    if sum == m:
        count += 1
print(count)



