def solution(files):
    answer = []
    separate = []
    for i,p in enumerate(files):
        head = ''
        number = ''
        for j,q in enumerate(p):
            if q.isdecimal():
                number += q
                if j == len(p)-1:
                    separate.append((head.lower(),number,i))
                else:
                    if not p[j+1].isdecimal:
                        print('hi')
                        separate.append((head.lower(),number,i))
                        break
            else:
                head += q
        print(head,number)
    separate = sorted(separate, key=lambda x:(x[0],int(x[1])))
    for i in separate:
        answer.append(files[i[2]])
    print(separate)
    return answer

solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])