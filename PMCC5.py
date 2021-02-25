import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
while True:
    if A[0] > A[-1]:
        A[0] -= 1
        A[2] -= 1
        A.pop(1)
    else:
        A[-1] -= 1
        A[-3] -= 1
        A.pop(-2)
    if len(A) < 3:
        break
print(max(A))