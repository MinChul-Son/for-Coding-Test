# https://programmers.co.kr/learn/courses/4008/lessons/13254
def solution(mylist):
    answer = [len(i) for i in mylist]
    return answer

def solution(mylist):
    return list(map(len, mylist))