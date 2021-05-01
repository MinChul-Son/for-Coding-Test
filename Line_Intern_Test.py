def solution(inputString):
    answer = 0
    small = 0
    medium = 0
    big = 0
    compare = 0
    stack = []
    is_exist = False
    for i,p in enumerate(inputString):
        if p == '(':
            is_exist = True
            small += 1
            stack.append((p, i))
        elif p == '{':
            is_exist = True
            medium += 1
            stack.append((p, i))
        elif p == '[':
            is_exist = True
            big += 1
            stack.append((p, i))
        elif p =='<':
            is_exist = True
            compare += 1
            stack.append((p, i))
        elif p == ')':
            small -= 1
            if small < 0 or stack[-1][0] != '(':
                return -i
            stack.pop()
            answer += 1
        elif p == '}':
            medium -= 1
            if medium < 0 or stack[-1][0] != '{':
                return -i
            stack.pop()
            answer += 1
        elif p == ']':
            big -= 1
            if big < 0 or stack[-1][0] != '[':
                return -i
            stack.pop()
            answer += 1
        elif p == '>':
            compare -= 1
            if compare < 0 or stack[-1][0] != '<':
                return -i
            stack.pop()
            answer += 1
    
    if not is_exist:
        return 0
    
    if stack:
        return -(len(inputString)-1)
    
    

    return answer



#----------------------------------------------------------------------------------
def solution(array):
    answer = []
    for i, p in enumerate(array):
        start = i
        end = i
        max_num = max(array)
        if max_num == p:
            answer.append(-1)
        else:
            while True:
                if array[start] <= p and start > 0:
                    start -= 1
                if array[end] <= p and end < len(array)-1:
                    end += 1
                
                if array[start] > p:
                    answer.append(start)
                    break
                if array[end] > p:
                    answer.append(end)
                    break
                
    return answer






#---------------------------------------------------------------------------------------------

def solution(ads):
    answer = 0
    timer = 0
    ads = sorted(ads, key=lambda x:(x[0], -x[1]))
    timer += ads[0][0] + 5
    ads.pop(0)

    while ads:
        scheduler = []
        for i in ads:
            if i[0] <= timer:
                scheduler.append(i)
        scheduler = sorted(scheduler, key=lambda x:x[1])
        current_process = scheduler.pop(-1)
        answer += (timer - current_process[0]) * current_process[1]
        timer += 5
        ads.remove(current_process)
    return answer
