# https://app.codility.com/c/run/trainingKBS29S-AX6/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary_num = str(format(N, 'b'))
    count = 0
    answer = 0

    for i in binary_num:
        if i == '1':
            if max_count < count:
                max_count = count
            count =0
        else :
            count +=1
            
    return answer
