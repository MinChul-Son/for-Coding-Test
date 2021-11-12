# https://app.codility.com/c/run/trainingKD3FRV-69T/

def solution(A):
    element_dic = dict()

    for i in A:
        if i in element_dic:
            element_dic[i] += 1
            continue
        element_dic[i] = 1
    
    for key, value in element_dic.items():
        if value % 2 == 1:
            return key