# https://app.codility.com/c/run/trainingEKYXS7-RK7/

def solution(A):
    A.sort()

    for i in range(len(A)):
        if A[i] == i + 1:
            continue
        return 0

    return 1