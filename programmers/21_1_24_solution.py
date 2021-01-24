# n = 1260
# count = 0
# array = [500, 100, 50, 10]
# for coin in array:
# 	count += n //coin
#     n %= coin
# print(count)


# N, K = map(int,(input().split()))
# count = 0
# while N != 1:
#     if N % K == 0:
#         N //= K
#     else:
#         N -= 1
#     count += 1
# print(count)


# s = input()
# cal_list = []
# for i in s:
#     if i == '0' or i == '1':
#         temp = i + '+'
#     else:
#         temp = i + '*'
#     cal_list.append(temp)
# cal_list[-1] = cal_list[-1][:-1]
# temp = "".join(cal_list)
# print(eval(temp))


# n = int(input())
# nums_list = list(map(int,input().split()))
# nums_list.sort()
# group = 0

# while True:
#     if not nums_list:
#         break
#     temp = nums_list.pop()
#     if temp-1 > len(nums_list):
#         continue
#     for _ in range(temp-1):
#         nums_list.pop()
#     group += 1
# print(group)

# n = int(input())
# data = list(map(int,input().split()))
# data.sort()
# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수
# for i in data: #공포도를 낮은 것부터 하나씩 확인
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹결성
#         result += 1
#         count = 0
# print(result)




