import math

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료    
    supplyPrice = orderAmount - taxFreeAmount - serviceFee
    if supplyPrice == 1:
        return 0
    return math.ceil(supplyPrice / 10)

#----------------------------------------------------------


def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    server_check = 0
    if sticky:
        sticky_check = 0
        last_server = 0
        for i in requests:
            server_check %= servers
            if i == sticky_check:
                answer[last_server].append(i)
                server_check = last_server
            else:
                answer[server_check].append(i)
            last_server = server_check
            server_check += 1
            sticky_check = i
    else:
        for i in requests:
            server_check %= servers
            answer[server_check].append(i)
            server_check += 1
    return answer

print(solution(2, True, [1,2,2,3,4,1]))

#----------------------------------------------
def solution(amountText):
    if amountText[0] == "," or amountText[-1] == ",":
        return False
    if amountText != "0" and amountText[0] == "0":
        return False
    seperator_count = 0
    for i, p in enumerate(reversed(amountText)):
        if p != "," and not p.isdigit() :
            return False
        if p == ",":
            if seperator_count != 3:
                return False
            seperator_count = 0
        seperator_count += 1
    return True


#------------------------------------------------
def solution(fruitWeights, k):
    answer = set()
    for i in range(len(fruitWeights)-k+1):
        answer.add(max(fruitWeights[i:i+k]))
    answer = list(answer)
    return sorted(answer, reverse=True)