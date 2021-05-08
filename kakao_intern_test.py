def solution(s):
    answer = ""
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    make_num = ""
    for i in s:
        if i.isdecimal():
            answer += i
        else:
            make_num += i
            if num_dic.get(make_num) == None:
                continue
            answer += num_dic.get(make_num)
            make_num = ""
    return int(answer)

#-----------------------------------------------------------------------------------------------------------------------
from collections import deque
import copy
def solution(places):
    answer = []
    for graph in places:
        temp_places = copy.deepcopy(graph)
        temp_places = list(map(list, temp_places))
        for i,p in enumerate(temp_places):
            for j,q in enumerate(p):
                if q == 'P':
                    if bfs(temp_places, i, j) == 0:
                        break
            else:
                continue
            break
        else:
            answer.append(1)
            continue
        answer.append(0)
    print(answer)
    return answer


def bfs(temp_places, i, j):
    queue = deque()
    queue.append((i, j))
    temp_places[i][j] = 'checked'
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if temp_places[nx][ny] == 'X':
                continue
            if temp_places[nx][ny] == "O":
                temp_places[nx][ny] = '.'
                queue.append((nx, ny))
            elif temp_places[nx][ny] == 'P':
                if abs(i-nx) + abs(j-ny) <= 2:
                    return 0
    return 1

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
#----------------------------------------------------------------------------------------------------
def solution(n, start, end, roads, traps):
    answer = 0
    current_num = start
    roads = sorted(roads, key=lambda x: (x[2], x[0]))
    while current_num != end:
        for i in roads:
            if i[0] == current_num and i[1] != start:
                current_num = i[1]
                answer += i[2]
                break
        if current_num in traps:
            for i in roads:
                if i[0] == current_num:
                    i[0], i[1] = i[1], i[0]
                elif i[1] == current_num:
                    i[0], i[1] = i[1], i[0]
    return answer

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))