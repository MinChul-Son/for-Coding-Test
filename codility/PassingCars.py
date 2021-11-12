# https://app.codility.com/c/run/trainingQSE7UJ-6V6/

def solution(A):
    one_count = A.count(1)
    answer = 0

    if A[0] == 0:
        answer += one_count

    for i in range(1, len(A)):
        if A[i-1] == 1:
            one_count -= 1

        if A[i] == 0:
            answer += one_count
        
        if answer > 1000000000:
            return -1

    return answer