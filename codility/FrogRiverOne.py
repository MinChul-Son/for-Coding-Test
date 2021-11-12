# https://app.codility.com/c/run/training8WBFJ9-GFR/

def solution(X, A):
    leaves = [0] * (X + 1)
    count = 0
    for idx, leaf in enumerate(A):
        if leaves[leaf] == 0:
            leaves[leaf] = 1
            count += 1
            if count == X:
                return idx
    return -1