# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = ['',0]
    devide_hashTag = []
    for c in m:
        if c == '#':
            devide_hashTag.append(devide_hashTag.pop() + c)
        else:
            devide_hashTag.append(c)
    for i in musicinfos:
        info_split = list(i.split(","))
        # 재생시간 구하기
        t1_h, t1_m = map(int, info_split[0].split(":"))
        t2_h, t2_m = map(int, info_split[1].split(":"))
        play_time = (t2_h-t1_h)*60 + (t2_m-t1_m)
        melody_devide = []
        for j in info_split[3]:
            if j == '#':
                melody_devide.append(melody_devide.pop() + j)
            else:
                melody_devide.append(j)
        if play_time < len(melody_devide):
                melody_devide = melody_devide[:play_time]
        else:
            melody_devide = melody_devide*(play_time//len(melody_devide)) + melody_devide[:(play_time%len(melody_devide))]
        for i in range(len(melody_devide) - len(devide_hashTag) + 1):
            if ''.join(melody_devide[i:i+len(devide_hashTag)]) == ''.join(m) and play_time > answer[1]:
                answer = [info_split[2], play_time]
    if answer[1]:
        return answer[0]
    return '(None)'




print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))

