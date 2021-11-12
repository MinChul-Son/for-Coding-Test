# https://app.codility.com/c/run/trainingT9R57E-YFN/

def solution(A):
    total = sum(A)
    first_part = A[0]

    answer = abs(first_part - (total - first_part))

    for i in range(1, len(A)-1):
        first_part += A[i]
        answer = min(answer, abs(first_part - (total - first_part)))
    
    return answer
