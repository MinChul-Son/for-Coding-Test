#https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3


temp = list(map(str,[124,24,3,4,554]))
temp2 = list(map(int,[124,24,3,4,554]))
number_len = []
answer_list = []


# for i in range(len(temp)):
#     y = 1
#     x= len(temp[i])
#     for j in range(x-1):
#         y = y*10 
#     number_len.append(temp2[i]//y)
# answer_list.append(temp[number_len.index(max(number_len))])
# temp.remove(temp[number_len.index(max(number_len))])
# temp2.remove(temp2[number_len.index(max(number_len))])
# print(temp)

# print(temp2)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True) #1000 이하이므로 최대 3자리 이므로 문자열을 3번 반복한후 그것을 키 값으로 비교한다.

    return str(int(''.join(numbers))) #join 함수는 배열을 특정 문자로 구분하여 문자열로 변환해주는 함수이다.
