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
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        for i in range(8):
            a = x + move_x[i]
            b = y + move_y[i]      
            dfs(a, b)   
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    move_x = [1, -1, 0, 0, 1, -1, -1, 1]
    move_y = [0, 0, -1, 1, 1, 1, -1, -1]
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    print(result)



