# https://www.acmicpc.net/problem/1389
# from collections import deque

# def bfs(num,n):
#     bacon=[0]*(n+1)
#     visited=[num]
#     queue=deque()
#     queue.append(num)

#     while queue:
#         k=queue.popleft()
#         for i in relation[k]:
#             if i not in visited:
#                 bacon[i]=bacon[k]+1
#                 visited.append(i)
#                 queue.append(i)

#     return sum(bacon)


# n,m=map(int, input().split())
# relation={i:[] for i in range(1,n+1)}
# for i in range(m):
#     a,b=map(int, input().split())
#     relation[a].append(b)
#     relation[b].append(a)

# result=[]
# for num in range(1,n+1):
#     result.append(bfs(num,n))

# print(result.index(min(result))+1)


# https://www.acmicpc.net/problem/10451
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    graph = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for i,p in enumerate(list(map(int, input().split()))):
        graph[i+1] = p
    for i in range(1, n+1):
        queue = deque()
        queue.append(i)
        visited[i] = 1
        while queue:
            x = queue.popleft()
            if visited[graph[x]] == 0:
                visited[graph[x]] = 1
                queue.append(graph[x])
            else:
                if graph[x] == i:
                    count += 1
                    break
    print(count)
        