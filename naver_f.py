def solution(id_list, k):
    answer = 0

    purchase_dict = dict()

    for customers in id_list:
        today_list = []
        for customer in customers.split(" "):
            if customer in today_list:
                continue

            if customer not in purchase_dict:
                purchase_dict[customer] = 1
                answer += 1
                today_list.append(customer)
                continue

            if purchase_dict[customer] < k:
                answer += 1
                purchase_dict[customer] += 1
                today_list.append(customer)

    return answer


# -------------------------------------------------------------
def solution(n, jump):
    answer = []
    return answer


#--------------------------------------------------------------
def solution(logs):
    if len(logs) < 10:
        return ["None"]

    answer = []
    solved_dict = dict()

    for i in range(len(logs)):
        logs[i] = logs[i].split()

    logs = sorted(logs, key=lambda x: (int(x[0]), int(x[1])))

    for log in logs:
        solved_dict[log[0] + " " + log[1]] = log[2]
    

    doubt_dict = dict()

    for i in solved_dict.items():
        student, problem_number = i[0].split()
        if student in doubt_dict: 
            doubt_dict[student] += problem_number + "-" + i[1] + " "
            continue
        doubt_dict[student] = problem_number + "-" + i[1] + " "
    
    result_list = list(doubt_dict.items())

    for i in range(len(result_list)):
        for j in range(i+1, len(result_list)):
            if result_list[i][1] == result_list[j][1]:
                answer.append(result_list[i][0])
                answer.append(result_list[j][0])

    return sorted(list(set(answer)))

#--------------------------------------------------------------
def solution(board):
    answer = 0

    for i in range(1, len(board)):
        board[0][i] += board[0][i-1]
    
    for i in range(1, len(board)):
        board[i][0] += board[i-1][0]
    
    # 음수면 바꾸고 양수면 그대로?
    for i in range(1, len(board)):
        for j in range(1, len(board)):
            if board[i][j] == 0:
                board[i][j] += max(abs(board[i-1][j]), abs(board[i][j-1]))
                continue
            board[i][j] += max(board[i-1][j], board[i][j-1])

    return board[-1][-1]