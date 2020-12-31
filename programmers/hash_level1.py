def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for a in range(len(completion)):       
        if (participant[a]==completion[a]):          
            answer=""
        else:
            answer = "".join(participant[a])
            return answer
    answer="".join(participant[-1])

    return answer