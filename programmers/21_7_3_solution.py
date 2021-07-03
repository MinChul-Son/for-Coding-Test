# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
# def solution(info, query):
#     answer = []
#     return answer



def solution(info, query):
    answer = []
    for i, p in enumerate(info):
        info[i] = p.split()
    for i, p in enumerate(query):
        query[i] = p.split(" and ")

    for i, p in enumerate(query):
        query[i].extend(query[i][-1].split())
        query[i].pop(-3)

    for i in query:
        count = 0
        score = int(i[-1])
        for j in info:
            for k, p in enumerate(j):
                if i[k] == p or i[k] == '-':
                    continue
                if p.isdecimal() and int(p) >= score:
                    continue
                break
            else:
                count += 1
        answer.append(count)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])