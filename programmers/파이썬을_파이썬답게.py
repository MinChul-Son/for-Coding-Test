# https://programmers.co.kr/learn/courses/4008/lessons/13254
def solution(mylist):
    answer = [len(i) for i in mylist]
    return answer

def solution(mylist):
    return list(map(len, mylist))


num = '3212'
base = 5
answer = int(num, base)


s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬


import string 
num = int(input().strip())
if num:
    print(string.ascii_uppercase)
else:
    print(string.ascii_lowercase)


def solution(mylist):
    return list(map(list, zip(*mylist)))