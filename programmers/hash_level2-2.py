clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# kinds =[]
# answer = 1
# for i in clothes:
#     count = 0
#     temp = []
#     for j in range(len(clothes)):
#         if i[1] == clothes[j][1]:
#             count +=1
#     temp.append(count)
#     temp.append(i[1])
#     #print(temp)
#     if kinds.count(temp) == 0: 
#         kinds.append(temp)
#         answer = answer *temp[0]
#     else:
#         pass
# answer = len(clothes) + answer
# print(answer)

def solution(clothes):
    kinds =[]
    answer = 1
    for i in clothes:
        count = 0
        temp = []
        for j in range(len(clothes)):
            if i[1] == clothes[j][1]:
                count +=1
        temp.append(count)
        temp.append(i[1])
        if kinds.count(temp) == 0: 
            kinds.append(temp)
            answer = answer *(temp[0]+1)
        else:
            pass
    answer = answer -1
    return answer


