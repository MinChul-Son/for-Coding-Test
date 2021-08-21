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
def solution(s):
    nums = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    for key, value in nums.items():
        s = s.replace(key,value)

    return int(s)

def solution(s):
    answer = ""
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    make_num = ""
    for i in s:
        if i.isdecimal():
            answer += i
        else:
            make_num += i
            search_from_dic = num_dic.get(make_num)
            if search_from_dic == None:
                continue
            answer += search_from_dic
            make_num = ""
    return int(answer)


# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer