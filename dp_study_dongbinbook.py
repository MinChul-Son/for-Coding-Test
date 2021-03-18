#DP 동빈북
#피보나치 수열 : 탑다운 DP
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 DP)
def fibo(x):
    # 종료 조건(1 or 2일때 1 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있다면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않았다면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
print(fibo(99))


# 피보나치 수열 : 바텀업 DP
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100
# f(1) 과 f(2)는 1
d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수 반복문으로 구현(바텀업)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])

# 개미 전사 문제
n = int(input())
k = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = k[0]
dp[2] = max(k[0], k[1])
for i in range(3, n + 1):
    dp[i] = max(dp[i-1], k[i-1]+ dp[i-2])
print(dp[-1])



# 1로 만들기 문제
x = int(input())
dp = [0 for _ in range(x+1)]
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0 and dp[i] > dp[i//2] +1:
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] +1:
        dp[i] = dp[i//3] + 1
    if i % 5 == 0 and dp[i] > dp[i//5] +1:
        dp[i] = dp[i//5] + 1
print(dp[x])

# 답안 예시
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    #현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])


# 효율적인 화폐 구성 문제
n, m = map(int, input().split())
bills = [int(input()) for _ in range(n)]
dp = [10001 for _ in range(m+1)]
dp[0] = 0
for i in bills:
    for j in range(i, m+1):
        if dp[j - i] != 10001:
            dp[j] = min(dp[j], dp[j - i] + 1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
