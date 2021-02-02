# https://www.acmicpc.net/problem/18258
# from collections import deque
# import sys
# n = int(input())
# queue = deque()
# for _ in range(n):
#     i = sys.stdin.readline().split()
#     if i[0] == 'push':
#         queue.append(int(i[1]))
#     elif i[0] == 'pop':
#         if queue:
#             print(queue.popleft())
#         else:
#             print(-1)
#     elif i[0] == 'size':
#         print(len(queue))
#     elif i[0] == 'empty':
#         if queue:
#             print(0)
#         else:
#             print(1)
#     elif i[0] == 'front':
#         if queue:
#             print(queue[0])
#         else:
#             print(-1)
#     else:
#         if queue:
#             print(queue[-1])
#         else:
#             print(-1)


# https://www.acmicpc.net/problem/2164
# from collections import deque
# n = int(input())
# queue = deque()
# for i in range(1,n+1):
#     queue.append(i)
# while len(queue) > 1:
#     print(queue)
#     queue.popleft()
#     queue.append(queue.popleft())
# print(queue)

# https://www.acmicpc.net/problem/11866

# from collections import deque
# n, k = map(int, input().split())
# s = deque([i for i in range(1,n+1)])
# res = []
# while len(s) != 1:
#     for _ in range(k-1):
#         s.append(s.popleft())
#     res.append(s.popleft())
# res.append(s[0])
# print('<'+", ".join(map(str, res))+'>')


# https://www.acmicpc.net/problem/1966
from collections import deque
test_case = int(input())
for _ in range(test_case):
    queue = deque()
    count = 0
    n, m = map(int, input().split())
    important = list(map(int,input().split()))
    if n == 1:
        print(1)
    else:
        for i,p in enumerate(important):
            queue.append([p,i])
        while True:
            if queue[0][0] == (max(queue))[0]:
                count += 1
                if queue[0][1] == m:
                    break
                else:
                    queue.popleft()
            else:
                queue.append(queue.popleft())
        print(count)

