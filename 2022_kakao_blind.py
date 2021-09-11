# 1번 - 솔
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    mail =dict()
    for i in id_list:
        mail[i] = 0
    
    for i in range(len(report)):
        report[i] = report[i].split()

    report_dic = dict()

    for i in report:
        if i[1] in report_dic:
            report_dic[i[1]] += 1
            continue

        report_dic[i[1]] = 1
    
    suspension_users = []

    for i in list(report_dic.items()):
        if i[1] >= k:
            suspension_users.append(i[0])
    
    for i in suspension_users:
        for j in report:
            if j[1] == i:
                mail[j[0]] += 1

    return list(mail.values())

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)


# ------------------------------------
# 2번 - 솔
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    if base == 10:
        return str(num)
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def solution(n, k):
    answer = 0
    number = convert(n, k)
    # 소수 양쪽에 아무것도 없는 경우 : 즉 한자리 수
    if len(number) == 1:
        if is_prime_number(int(number)):
            return 1
        return 0
    # 그외
    temp = ''
    for i in range(len(number)):
        if number[i] != '0':
            temp += number[i]
            continue
        if not temp:
            continue
        if is_prime_number(int(temp)):
            answer += 1
        
        temp = ''
    if temp:
        if is_prime_number(int(temp)):
            answer += 1
    return answer

solution(123123, 7)

# -------------------------------------------------
# 3번 - 솔
import math

def solution(fees, records):
    answer = []
    parking = dict()
    times = dict()

    for i in records:
        temp = i.split()
        # 입차
        if temp[2] == 'IN':
            parking[temp[1]] = temp[0]
            continue
        
        # 주차 시간 계산
        out_list = temp[0].split(':') 
        in_list = parking[temp[1]].split(':')
        out_time_to_minute = int(out_list[0]) * 60 + int(out_list[1])
        in_time_to_minute = int(in_list[0]) * 60 + int(in_list[1])
        parking_time = out_time_to_minute - in_time_to_minute
        del parking[temp[1]]

        # 출차
        if temp[1] in times:
            times[temp[1]] += parking_time
            continue

        # 첫 이용
        times[temp[1]] = parking_time

    # 출차 기록이 없는 차량 추가 계산
    if parking:
        for i in list(parking.items()):
            in_list = i[1].split(':') 
            in_time_to_minute = int(in_list[0]) * 60 + int(in_list[1])
            out_time_to_minute = 23 * 60 + 59
            parking_time = out_time_to_minute - in_time_to_minute
            if i[0] in times:
                times[i[0]] += parking_time
                continue

            times[i[0]] = parking_time
    
    # 주차 요금 계산
    for i in sorted(list(times.items())):
        # 기본 시간 이하
        if i[1] <= fees[0]:
            answer.append(fees[1])
            continue
        # 기본 시간 초과
        answer.append(math.ceil((i[1]-fees[0])/fees[2]) * fees[3] + fees[1])


    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])


# --------------------------------------------------------
# 4번 - 못품 ==> 풀 수 있을 것 같은데 안되서 빡침;; (얘 때매 시간 다씀)

# def solution(n, info):
#     cadidate = []
#     count = 11
#     apeach_score = 0
#     if info[0] == n:
#         return [-1]

#     for i in range(count):
#         answer = [0 for _ in range(11)]
#         copy_n = n
#         score = 0
#         for j in range(i, 11):
#             if copy_n > info[j]:
#                 answer[j] = info[j] + 1
#                 score += (10-j)
#                 copy_n -= info[j] + 1
#         if copy_n > 0:
#             answer[-1] = copy_n
#             copy_n = 0
#         cadidate.append([answer, score])
#     cadidate = sorted(cadidate, key=lambda x: (-x[1], x[0]))
#     return cadidate[0][0]

def solution(n, info):
    cadidate = []
    count = 11
    apeach_score = 0
    if info[0] == n:
        return [-1]
    answer = [0 for _ in range(11)]
    copy_n = n
    score = 0
    for i in range(count):
        if copy_n > info[i]:
            answer[i] = info[i] + 1
            score += (10-i)
            copy_n -= answer[i]
    if copy_n > 0:
        answer[-1] = copy_n
        copy_n = 0
        
    cadidate.append([answer, score])
    
    cadidate = sorted(cadidate, key=lambda x: (-x[1], x[0]))
    print(cadidate)
    return cadidate[0][0]

solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])


#------------------------------------------------------
# 5번 - 못품
def solution(info, edges):
    answer = 0
    sheep = 0
    wolf = 0
    tree = [[] for _ in range(len(info))]
    for i in edges:
        tree[i[0]].append(i[1])
    

    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])

#------------------------------------------------------
# 6번 - 정확성 통과, 효율성 통과x ==> 0.5솔
import numpy
def solution(board, skill):
    answer = 0
    skill_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in skill:
        if i[0] == 1:
            for r in range(i[1], i[3]+1):
                for c in range(i[2], i[4]+1):
                    skill_board[r][c] -= i[5]
        else:
            for r in range(i[1], i[3]+1):
                for c in range(i[2], i[4]+1):
                    skill_board[r][c] += i[5]

    answer_board = (numpy.array(board) + numpy.array(skill_board)).tolist()
    for i in answer_board:
        for j in i:
            if j > 0:
                answer += 1
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])


# --------------------------------------------------------
# 7번 - 못품
def solution(board, aloc, bloc):
    answer = -1
    if len(board) == 1:
        if len(board[0]) == 1:
            return 0
        return len(board[0]) - 1
    return answer