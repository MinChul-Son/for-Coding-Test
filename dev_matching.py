def solution(registered_list, new_id):
    answer = new_id
    S = ''
    N = ''
    for i in new_id:
        if i.isalpha():
            S += i
        else:
            N += i
    if not N:
        N = '0'
    
    dictionary = dict.fromkeys(registered_list,0)

    while True:
        if answer in dictionary:
            N = str(int(N) + 1)
            answer = S + N
            continue
        break
    return answer

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))


# -------------------------------------------------------------
def solution(leave, day, holidays):
    answer = -1
    return answer