# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

# def solution(d, budget):
#     answer = 0
#     d.sort()
#     for i,p in enumerate(d):
#         if budget==0:
#             break
#         if p <= budget:
#             budget -= p
#             answer += 1
#         else:
#             break    
#     return answer


# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
# from operator import itemgetter

# def solution(N, stages):
#     temp_list = []
#     answer = []

#     for i in range(1,N+1):
#         entire_people = 0
#         ing_people = stages.count(i)
#         for j in stages:
#             if j >= i:
#                 entire_people += 1
#         if entire_people == 0:
#             temp_list.append((0,i))
#         else:
#             temp_list.append((ing_people/entire_people,i))
#     temp_list = sorted(temp_list, key=itemgetter(0), reverse= True)
#     sorted(temp_list, key=itemgetter(1))
#     for i in range(len(temp_list)):
#         answer.append(temp_list[i][1])
#     return answer

# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
# def solution(n, arr1, arr2):
#     temp_list = []
#     answer = []
#     for i in range(0,n):
#         arr1[i]= format(arr1[i],'b')
#         arr1[i] ="0"*(n-len(arr1[i])) + arr1[i]
#         arr2[i]= format(arr2[i],'b')
#         arr2[i] ="0"*(n-len(arr2[i])) + arr2[i]

#     temp_list = list(zip(arr1,arr2))

#     for i in temp_list:
#         temp_str = ""
#         for j in range(n):
#             if (int(i[0][j:j+1])+int(i[1][j:j+1]))>0:
#                 temp_str += "#"
#             else:
#                 temp_str += " "
#         answer.append(temp_str)
#     return answer