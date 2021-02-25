import sys
from collections import deque
N = int(sys.stdin.readline())
A = deque(map(int, sys.stdin.readline().split()))
while len(A) > 2:
    if A[0] > A[-1]:
        A[0] -= 1
        A[2] -= 1
        temp = A.popleft()
        A.popleft()
        A.appendleft(temp)
    else:
        A[-1] -= 1
        A[-3] -= 1
        temp = A.pop()
        A.pop()
        A.append(temp)
print(max(A))