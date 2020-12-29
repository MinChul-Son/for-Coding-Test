#https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

# citations = [3, 0, 6, 1, 5]
# cit_num = len(citations) # 논문의 갯수
# max_num = 0
# dasf= sorted(citations, reverse=True)
# print(dasf)
# temp = 0
# for j in range(cit_num): 
#     temp = citations[j]
#     count2 = 0
#     for i in range(cit_num):
#         count = 0
#         if temp <= citations[i]:
#             count +=1
#             count2 += count
#             print(count2)
            
#         else:
#             pass
#         if max_num<count2:
#             max_num = count2
    
    
    
# answer = max_num
# print(answer)


#답
def solution3(citations):
    citations = sorted(citations) # 오름차순으로 정렬
    for idx in range(len(citations)):
    # (len(citations) - idx) : citations[idx] 번 이상 인용된 논문의 개수를 의미
        if citations[idx] >= len(citations) - idx: 
            return (len(citations) - idx)