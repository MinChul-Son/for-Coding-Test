# https://www.acmicpc.net/problem/1712
# A, B, C = list(map(int, input().split()))
# BREAK_EVEN_POINT = 0

# if(C <= B):
#     BREAK_EVEN_POINT = -1
# else:
#     BREAK_EVEN_POINT = A // (C - B) + 1 
# print(BREAK_EVEN_POINT)


# https://www.acmicpc.net/problem/2292
# n = int(input())
# cnt = 1
# cnt_six = 6
# count = 1
# while n > cnt:
#     count += 1
#     cnt += cnt_six
#     cnt_six += 6
# print(count)


# https://www.acmicpc.net/problem/13305
# n = int(input())
# path = list(map(int, input().split()))
# cost = list(map(int, input().split()))
# sum_cost = 0
# # 나보다 오른쪽 도시의 기름값이 더 싼곳(맨 끝값은 제외)이 있다면 거리만큼만 기름 충전, 없다면 남은 거리 싹다 충전해버리기
# temp = cost[0]
# for i in range(n-1):
#     if cost[i] <= temp:
#         temp = cost[i]
#     sum_cost += temp*path[i]
# print(sum_cost)


# https://www.acmicpc.net/problem/11721
# n = input()
# for i,p in enumerate(n):
#     print(p, end="")
#     if str(i)[-1] == '9':
#         print("")

# https://www.acmicpc.net/problem/11719
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break


