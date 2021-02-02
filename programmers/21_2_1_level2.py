import re
def solution(files):
    answer = [re.split(r"([0-9]+)",s) for s in files]
    sort = sorted(answer, key=lambda x:(x[0].lower(),int(x[1])))
    return ["".join(s) for s in sort]
    

solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])