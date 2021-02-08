# https://www.acmicpc.net/problem/1110
N = int(input())
cycle = 0
new_num = N
while True:
    temp = str(new_num)
    cycle += 1
    if int(temp) < 10:
        new_num = int(temp + temp)
    else:
        new_num = int(temp[-1] + str(int(temp[0]) + int(temp[1]))[-1])
    if new_num == N:
        break
print(cycle)