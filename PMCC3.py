import sys
N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
pay = 0
select = True
if A[0] < B[0]:
    pay += A[0]
else:
    pay += B[0]
    select = False
for i in range(1, N-1):
    if select:
        if A[i] > B[i] + K:
            select = False
            pay += B[i] + K
        else:
            pay += A[i]
    else:
        if A[i] + K < B[i]:
            select = True
            pay += A[i] + K
        else:
            pay += B[i]
print(pay)
