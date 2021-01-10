#https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

# from datetime import datetime as date

# print(date.today().strftime("%A"))

# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%A"))
# import datetime 
# import calendar 
  
# def findDay(a,b):
#     date = '2016 '+str(a)+' '+str(b) 
#     day = datetime.datetime.strptime(date, '%Y %m %d').weekday() 
#     return (calendar.day_name[day][:3]).upper() 
  
# # Driver program 
# print(findDay(5,24)) 


# #------------------------------------------------------------------
# #https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

# def solution(s):
#     if len(s)%2 == 1:
#         return s[int(len(s)/2):int(len(s)/2)+1]
#     else:
#         return s[int(len(s)/2)-1:int(len(s)/2)+1]




# #----------------------------------------------------------
# #https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

# from itertools import permutations

# def solution(numbers):
#     answer = []
#     combination_list = list(permutations(numbers,2))
#     for i in range(len(combination_list)):
#         answer.append(int(combination_list[i][0])+int(combination_list[i][1]))
#     answer = list(set(answer))
#     answer.sort()
#     return answer


#--------------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

# def solution(n):
#     answer = ''
#     while n > 0:
#         n -= 1
#         answer = '124'[n%3] + answer
#         n //= 3
#     return answer


# #---------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

# def solution(skill, skill_trees):
#     answer = 0
#     pop_trees = []
#     skill = list(skill)
#     match_list = []
#     i = 0
#     while skill_trees :
#         match_list = []
#         pop_trees = list(skill_trees[0])
#         skill_trees.pop(0)
#         for j in skill:
#             match_list.append(pop_trees.index(j))
#         is_sorted = (sorted(match_list) == match_list)
#         if is_sorted:
#             answer += 1
#         else:
#             pass
#         i += 1
#     return answer

# skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# length_trees = len(skill_trees)
# answer = 0
# pop_trees = []
# skill = list(skill)
# i = 0
# while i<length_trees:
#     print(skill_trees)
#     procedure_bool = True
#     match_list = []
#     pop_trees = list(skill_trees[0])
#     print(pop_trees)
#     skill_trees.pop(0)
#     for j,p in enumerate(skill):
#         if p in pop_trees:
#             match_list.append(pop_trees.index(p))
#         else:
#             if p == skill[0]:
#                 procedure_bool = False
#                 break
#             elif p == skill[-1]:
#                 pass
#             else:
#                 temp_list= skill[j+1:]
#                 for k in temp_list:
#                     if k in pop_trees:
#                         procedure_bool = False
#                         break
#     print(match_list)
#     if procedure_bool:
#         pass
#     else:
#         i += 1
#         continue
#     is_sorted = (sorted(match_list) == match_list)
#     if is_sorted:
#         answer += 1
#     else:
#         pass
    
#     print(is_sorted)
    
#     i += 1
# print(answer)

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        tree = list(tree)
        skill_list = list(skill) #skill string을 list로 변환
        chk = True
        while tree:
            item = tree.pop(0)
            if item in skill_list:
                s = skill_list.pop(0)
                if s != item:
                    chk = False
                    break
        if chk:
            answer += 1
        
            
    return answer