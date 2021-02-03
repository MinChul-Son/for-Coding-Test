# https://www.acmicpc.net/problem/1003

n = int(input())
count0=[1,0,1]
count1=[0,1,1]

def fibonacci (k):
    if len(count0) <= k:
        for i in range(len(count0), k+1):
            count0.append(count0[i-1]+count0[i-2])
            count1.append(count1[i-1]+count1[i-2])
    print(count0[k],count1[k])

for _ in range(n):
    N = int(input())
    fibonacci(N)
