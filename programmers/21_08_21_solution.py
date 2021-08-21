# https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    answer = 0
    for n in range(1, count+1):
        answer += (price * n)

    return abs(money-answer) if money-answer < 0 else 0 


# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def solution(lottos, win_nums):
    ranking = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4: 3, 5 : 2, 6 : 1}
    answer = []
    zero_count = lottos.count(0)
    is_same_count = 0
    for i in lottos:
        if i == 0:
            continue
        if i in win_nums:
            is_same_count += 1
    answer.append(ranking[is_same_count+zero_count])
    answer.append(ranking[is_same_count])

    return answer

# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
