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