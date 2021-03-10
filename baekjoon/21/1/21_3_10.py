# https://www.acmicpc.net/problem/9184
# def solution(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return solution(20, 20, 20)

#     if dp[a][b][c]:
#         return dp[a][b][c]
#     if a<b<c :
#         dp[a][b][c] = solution(a,b,c-1) + solution(a,b-1,c-1) - solution(a,b-1,c)
#     else:
#         dp[a][b][c] = solution(a-1,b,c) + solution(a-1,b-1,c) + solution(a-1,b,c-1) - solution(a-1,b-1,c-1)
#     return dp[a][b][c]
    

# while True:
#     a, b, c = map(int, input().split())
#     dp = [[[0]*21 for _ in range(21)] for __ in range(21)]
#     if a == -1 and b == -1 and c == -1:
#         break
#     print("w(%d, %d, %d) = %d"%(a, b, c, solution(a, b, c)))


# https://www.acmicpc.net/problem/1300
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) 
    
    if temp >= K: 
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)