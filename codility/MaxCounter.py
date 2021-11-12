# https://app.codility.com/c/run/trainingNW5B4E-KSU/

def solution(N, A):
    counter_dic = {i:0 for i in range(1,N+1)}
    counter_store = 0
    max_counter = 0
    for key in A:
        if key == N+1:
            counter_store += max_counter
            counter_dic.clear()
            max_counter = 0
        else:
            if counter_dic.get(key) is None:
                counter_dic[key] = 1
            else:
                counter_dic[key] += 1
                
            max_counter = max(max_counter,counter_dic[key])
    
    answer = [counter_store] * N
    for key,val in counter_dic.items():
        answer[key-1] += val 
    
    return answer