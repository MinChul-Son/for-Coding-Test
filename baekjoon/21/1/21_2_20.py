# https://www.acmicpc.net/problem/1717
# n, m = map(int, input().split())
# union_set = {i for i in range(n+1)}
# temp_list = []
# for _ in range(m):
#     input_num = list(map(int, input().split()))
#     if input_num[0] == 0:
#         if input_num[1] == input_num[2]:
#             if input_num[1] in union_set:
#                 union_set.discard(input_num[1])
#                 temp_list.append([input_num[1]])
#                 continue
#             else:
#                 continue
#         if input_num[1] in union_set and input_num[2] in union_set:
#             union_set.discard(input_num[1])
#             union_set.discard(input_num[2]) 
#             temp_list.append([input_num[1],input_num[2]])
#         elif input_num[1] in union_set:
#             for i, p in enumerate(temp_list):
#                 if input_num[2] in p:
#                     temp_list[i].append(input_num[1])
#         elif input_num[2] in union_set:
#             for i, p in enumerate(temp_list):
#                 if input_num[1] in p:
#                     temp_list[i].append(input_num[2])
#         else:
#             a_idx = 0
#             b_idx = 0
#             for i,p in enumerate(temp_list):
#                 if input_num[1] in p:
#                     a_idx = i
#                 elif input_num[2] in p:
#                     b_idx = i
#             temp_list[a_idx].extend(temp_list[b_idx])
#             temp_list.pop(b_idx)
#     else:
#         for i in temp_list:
#             if input_num[1] in i and input_num[2] in i:
#                 print("YES")
#                 break
#         else:
#             print("NO")
#     print(union_set, temp_list)



# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# parent = [ i for i in range(n + 1)]
# def find(target):
#     if target == parent[target]:
#         return target

#     parent[target] = find(parent[target])
#     return parent[target]

# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# for _ in range(m):
#     oper, a, b = map(int, input().split())
#     if oper:
#         if find(a) == find(b):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         union(a, b)
#     print(parent)



# https://www.acmicpc.net/problem/5430
# import sys
# from collections import deque
# t = int(input())

# for _ in range(t):
#     p = sys.stdin.readline().strip()
#     n = int(sys.stdin.readline())
#     temp_list = sys.stdin.readline().strip().split(",")
#     if p.count('D') > n:
#         print("error")
#         continue
#     temp_list[0] = temp_list[0][1:]
#     temp_list[-1] = temp_list[-1][:-1]
#     temp_list = deque(temp_list)
#     for i in p:
#         if i == 'R':
#             temp_list.reverse()
#         else:
#             temp_list.popleft()
#     temp_list = list(map(int, temp_list))
#     print(temp_list)



# import sys 
# import re 
# from collections import deque 
# T = int(sys.stdin.readline()) 
# for _ in range(T): 
#     P = list(sys.stdin.readline()) 
#     N = int(sys.stdin.readline()) 
#     input = sys.stdin.readline() 
#     arr = re.split("\[|\]|,|\n", input) 
#     print(arr)
#     arr = deque(arr[1:-2]) 
#     if N == 0: 
#         arr = deque([]) 
#     r_flag = False 
#     oob = False 
#     for p in P: 
#         if p == "R": 
#             r_flag = not r_flag 
#         elif p == "D": 
#             if len(arr) == 0: 
#                 oob = True 
#                 break 
#             if r_flag: 
#                 arr.pop() 
#             else: 
#                 arr.popleft() 
#     if oob: 
#         print("error") 
#     else: 
#         arr = list(arr) 
#         if r_flag: 
#             arr.reverse() 
#         print("[", end = "") 
#         print(",".join(arr), end = "") 
#         print("]")




# case = int(input())

# for _ in range(case):
#     function = list(input())
#     num = int(input())
#     arr = eval(input())
    
#     error = False
#     R_count = 0 #홀/짝 뒤집힌 횟수용
#     D_front = 0 #앞에서 없어지는 수
    
#     for func in function:            
#         if func == 'R':
#             R_count += 1
#         else:
#             try:
#                 if R_count % 2 == 0:
#                     D_front += 1 #앞에서는 슬라이싱으로 나중에 뺴줌
#                 else:
#                     arr.pop() #이건 뒤에서 바로 뺴줌
#             except:
#                 error = True
#                 break
                
#     #에러 걸러주기
#     if error or D_front > len(arr):
#         print('error')
#         continue
        
#     #R개수에 따른 정답 변형
#     if R_count % 2 == 0:
#         answer = arr[D_front:]
#     else:
#         answer = list(reversed(arr[D_front:]))
        
#     #출력함수
#     print("[", end='')
#     for i in range(len(answer)):
#         if i == len(answer) - 1:
#             print(answer[i], end = '')
#         else:
#             print("%s," %(answer[i]), end='')
#     print("]")