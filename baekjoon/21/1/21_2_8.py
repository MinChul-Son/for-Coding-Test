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
# n = int(input())
# count = 0
# while n >= 0:
#     if n % 5 == 0:
#         count += (n//5)
#         print(count)
#         break
#     n -= 3
#     count += 1
# else:
#     print(-1)

# https://www.acmicpc.net/problem/1546
# n = int(input())
# score = list(map(int, input().split()))
# score.sort()
# new_score = []
# for i in range(n):
#     new_score.append(score[i]/score[-1]*100)
# print(sum(new_score)/n)

# https://www.acmicpc.net/problem/4344
# c = int(input())
# for _ in range(c):
#     n = list(map(int, input().split()))
#     student = n.pop(0)
#     count = 0
#     avg = sum(n) / student
#     for i in n:
#         if i > avg:
#             count += 1
#     percent = round(count/student*100,3)
#     print('%.3f%%' %percent)


# https://www.acmicpc.net/problem/4673
# num_list = [0 for _ in range(20001)]
# for i in range(1,10001):
#     temp = list(map(int,list(str(i))))
#     self_num = i + sum(temp)
#     num_list[self_num] += 1
# for i in range(1,10001):
#     if num_list[i] == 0:
#         print(i)

# https://www.acmicpc.net/problem/1924
# import datetime
# day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# x , y = map(int, input().split())
# print(day[datetime.date(2007,x,y).weekday()])