def solution(arr):
    answer = 0
    current_ball = 0

    for i in arr:
        current_ball += i
        if current_ball > 0:
            answer += 1
    return answer


#--------------------------------------
import math

def solution(x, y):
    bridges = []
    islands = zip(x, y)
    islands = sorted(islands, key=lambda x: (x[0], x[1]))
    print(islands)

    for i in range(len(x) - 1):
        bridges.append(math.sqrt(math.pow(islands[i][0] - islands[i+1][0], 2) + math.pow(islands[i][1] - islands[i+1][1], 2)))
    return math.ceil(max(bridges))

#------------------------------------------
def solution(pixels):
    answer = ''
    number_dic = {
        ('111','101', '101', '101', '111') : '0',
        ('110', '010', '010', '010', '111') : '1', 
        ('111', '001', '111', '100', '111') : '2',
        ('111', '001', '111', '001', '111') : '3',
        ('101', '101', '111', '001', '001') : '4',
        ('111', '100', '111', '001', '111') : '5',
        ('111', '100', '111', '101', '111') : '6',
        ('111', '101', '001', '001', '001') : '7',
        ('111', '101', '111', '101', '111') : '8',
        ('111', '101', '111', '001', '111') : '9'
    }

    for i in range(0, len(pixels[0]), 3):
        tmp = (pixels[0][i:i+3], pixels[1][i:i+3], pixels[2][i:i+3], pixels[3][i:i+3], pixels[4][i:i+3])
        answer += number_dic.get(tmp)
    return answer

# ----------------------------------------------
from itertools import combinations

def solution(needs, r):
    finished = []
    components = [i for i in range(len(needs[0]))]
    component_combi = list(combinations(components, r))
    
    for combi in component_combi:
        answer = 0
        for i in range(len(needs)):
            for j in range(len(needs[0])):
                if needs[i][j] == 1 and j not in combi:
                    break
            else:
                answer += 1
        finished.append(answer)

    return max(finished)

#---------------------------------------------------
def solution(strs):
    answer = -1

    return answer