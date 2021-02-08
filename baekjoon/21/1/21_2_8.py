# https://www.acmicpc.net/problem/1110
# N = int(input())
# cycle = 0
# new_num = N
# while True:
#     temp = str(new_num)
#     cycle += 1
#     if int(temp) < 10:
#         new_num = int(temp + temp)
#     else:
#         new_num = int(temp[-1] + str(int(temp[0]) + int(temp[1]))[-1])
#     if new_num == N:
#         break
# print(cycle)

# https://www.acmicpc.net/problem/2839
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)