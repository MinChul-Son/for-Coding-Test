#prices = [1, 2, 3, 2, 3]
#x = 0
#answer = []
#answer = [0] * len(prices)
# count =0
# temp = prices.copy()
# for i in range(len(prices)-1):   
#     if prices[i] <=  
# answer.append(0)
# print(temp)

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):        
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer
