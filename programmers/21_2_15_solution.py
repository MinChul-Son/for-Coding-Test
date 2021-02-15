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
# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     for i in course:
#         combi_list = []
#         count_list = []
#         for j in orders:
#             if len(j) < i:
#                 continue
#             temp = list(combinations(sorted(list(j)),i))
#             combi_list.extend(temp)
#         for j in set(combi_list):
#             count_list.append((combi_list.count(j),j))
#         count_list.sort(reverse=True)
#         for j in range(0,len(count_list)-1):
#             if count_list[j][0] == 1:
#                 break
#             if count_list[j][0] != count_list[j+1][0]:
#                 answer.append("".join(count_list[j][1]))
#                 break
#             else:
#                 answer.append("".join(count_list[j][1]))
#         answer.sort()
#     return answer

# solution(["XYZ", "XWY", "WXA"],[2,3,4])


# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

def solution(info, query):
    answer = []
    for i, p in enumerate(info):
        info[i] = p.split()
    for i, p in enumerate(query):
        query[i] = p.split("and")
    for i, p in enumerate(query):
        query[i].extend(query[i][-1].split())
        query[i].pop(-3)
    for i,q in enumerate(query):
        for j,p in enumerate(q):
            query[i][j] = p.strip()
    for i in query:
        count = 0
        score = int(i[-1])
        temp = []
        for j in info:
            if int(j[-1]) >= score:
                temp.append(j)
        if '-' in i:
            del_list = []
            for j in i[:-1]:
                if j == '-':
                    pass
                else:
                    for k in temp:
                        if j in k:
                            pass
                        else:
                            del_list.append(k)
            for i in del_list:
                temp.remove(i)
            answer.append(len(temp))
        else:
            for j in temp:
                if i[:-1] == j[:-1]:
                    count += 1
            answer.append(count)

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])