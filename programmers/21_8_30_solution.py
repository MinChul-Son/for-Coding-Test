# https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3
def solution(s):
    convert_count = 0
    remove_count = 0
    while True:
        if s == '1':
            break
        convert_count += 1
        remove_count += s.count('0')
        s = s.replace('0', "")
        s = str(format(len(s), 'b'))
    return [convert_count, remove_count]

solution("110010101001")