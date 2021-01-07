def solution(answers):
    answer = []
    student1 = [1,2,3,4,5] *8
    student2 = [2,1,2,3,2,4,2,5] * 5
    student3 = [3,3,1,1,2,2,4,4,5,5] * 4
    rank_list = [0,0,0]
    count = 0
    max_count = 0
    while count<len(answers):
        if count==len(student1): #각 학생별 규칙이 모지랄 때
            student1 = student1 *2
            student2 = student2 *2
            student3 = student3 *2
        if answers[count] == student1[count]:
            rank_list[0] += 1
        if answers[count] == student2[count]:
            rank_list[1] += 1
        if answers[count] == student3[count]:
            rank_list[2] += 1     
        count += 1
    
    max_count = max(rank_list)
    for i in range(len(rank_list)):
        if rank_list[i] == max_count:
            answer.append(i+1)
    
    return answer
print(solution([1,3,2,4,2]))


