# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# def solution(new_id):
#     answer = ''
#     new_id = list(new_id.lower())
#     temp = ''
#     for i,p in enumerate(new_id):
#         if not p.isalpha():
#             if p == '-' or p == '_' or p== '.':
#                 temp += p
#             elif p.isdecimal():
#                 temp += p
#             else:
#                 pass
#         else:
#             temp += p
#     new_id = temp
#     while True:
#         if ".." in new_id:
#             new_id = new_id.replace("..", ".")
#         else:
#             break
#     if new_id[0] == '.':
#         new_id = new_id[1:]
#     elif new_id[-1] == '.':
#         new_id = new_id[:-1]
#     if not new_id:
#         new_id += 'a'
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#     while True:
#         if new_id[-1] == '.':
#             new_id = new_id[:-1]
#         else:
#             break
#     if len(new_id) <= 2:
#         while len(new_id) < 3:
#             new_id += new_id[-1]
#     return new_id

# solution("abcdefghijklmn.p")


# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        combi_list = []
        count_list = []
        for j in orders:
            if len(j) < i:
                continue
            temp = list(combinations(sorted(list(j)),i))
            combi_list.extend(temp)
        for j in set(combi_list):
            count_list.append((combi_list.count(j),j))
        count_list.sort(reverse=True)
        for j in range(0,len(count_list)-1):
            if count_list[j][0] == 1:
                break
            if count_list[j][0] != count_list[j+1][0]:
                answer.append("".join(count_list[j][1]))
                break
            else:
                answer.append("".join(count_list[j][1]))
        answer.sort()
    print(answer)
    return answer

solution(["XYZ", "XWY", "WXA"],[2,3,4])