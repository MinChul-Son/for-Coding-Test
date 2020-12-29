#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    list= []
    i = 0
    j = 0
    k = 0
    answer = []
    for m in range(0,len(commands)):
        for n in range(0,3):
            if n == 0:
                i = commands[m][n] -1 
            elif n == 1:
                j = commands[m][n]
            else:
                k = commands[m][n]
        temp = array[i:j]
        list = sorted(temp)
        answer.append(list[k-1])                                
    
    return answer