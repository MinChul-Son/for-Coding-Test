# https://app.codility.com/c/run/trainingRTF5UY-5JJ/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

def solution(A, K):
    if K % len(A) == 0:
        return A

    rotate_list = deque(A)
    rotate_list.rotate(K)

    return list(rotate_list)
    
    

solution([1,2,3,4], 5)