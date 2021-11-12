# https://app.codility.com/c/run/trainingF4JGEJ-6M6/

def solution(A):
    if not A:
        return 1

    return sum(range(1, len(A)+2)) - sum(A)