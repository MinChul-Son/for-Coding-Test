user_input = input()
n, m = map(int, user_input.split())

print(n*m)

#----------------------------------------

import sys
from collections import deque

input = sys.stdin.readline
goorm_forest = []

for _ in range(10):
    goorm_forest.append(list(input().strip()))

# 윤성이 위치 찾기

yoonsung_x, yoonsung_y = 0, 0

for i in range(10):
    for j in range(10):
        if goorm_forest[i][j] == 'H':
            yoonsung_x = i
            yoonsung_y = j

# 윤성이 위치를 시작점으로 설정
goorm_forest[yoonsung_x][yoonsung_y] = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
                continue

            if goorm_forest[nx][ny] == 'R':
                continue

            if goorm_forest[nx][ny] == '.':
                goorm_forest[nx][ny] = goorm_forest[x][y] + 1
                queue.append((nx, ny))
            
            if goorm_forest[nx][ny] == 'M':
                return goorm_forest[x][y]

print(bfs(yoonsung_x, yoonsung_y))


# ---------------------------------------------------------
import copy

penguins = list(map(int, input().split()))

min_move = 0
max_move = 0

# 아이디어
# 1. 1,2 그리고 2,3 번째 중 차이가 더 많이 나는 쪽에 집어넣으면 max
#   1-1. 차이가 많이 나는 쪽의 바로 다음 위치에 넣어줘야함
#       ==> 1 3 8 있을 때 오른쪽 펭귄을 4로 이동시켜 3 4 8 로
# 2. 차이가 더 작은 쪽에 집어넣으면 min
#   2-1. 차이가 1이라면 못들어감, 이 경우에는 무조건 반대쪽에 넣어줘야함

copy_penguins = copy.deepcopy(penguins)

# 최대값 구하기
while True:
    if copy_penguins[1] - copy_penguins[0] >= copy_penguins[2] - copy_penguins[1]:
        if copy_penguins[1] - copy_penguins[0] == 1:
            break
        tmp = copy_penguins[1]
        copy_penguins[1] = copy_penguins[0] + 1
        copy_penguins[2] = tmp
        max_move += 1

    else:
        tmp = copy_penguins[1]
        copy_penguins[1] = copy_penguins[1] + 1
        copy_penguins[0] = tmp
        max_move += 1
        

    if copy_penguins[0] + 1 == copy_penguins[1] and copy_penguins[1] + 1 == copy_penguins[2]:
        break


# 최소값 구하기
copy_penguins = copy.deepcopy(penguins)

while True:
    if copy_penguins[1] - copy_penguins[0] >= copy_penguins[2] - copy_penguins[1]:
        if copy_penguins[1] - copy_penguins[0] == 1:
            break

        if copy_penguins[2] - copy_penguins[1] == 1:
            tmp = copy_penguins[1]
            copy_penguins[1] = (copy_penguins[0] + copy_penguins[1]) // 2
            copy_penguins[2] = tmp
            min_move += 1
        else:
            tmp = copy_penguins[1]
            copy_penguins[1] = (copy_penguins[1] + copy_penguins[2]) // 2
            copy_penguins[0] = tmp
            min_move += 1

    else:
        if copy_penguins[1] - copy_penguins[0] == 1:
            tmp = copy_penguins[1]
            copy_penguins[1] = (copy_penguins[1] + copy_penguins[2]) // 2
            copy_penguins[0] = tmp
            min_move += 1
        else:
            tmp = copy_penguins[1]
            copy_penguins[1] = (copy_penguins[0] + copy_penguins[1]) // 2
            copy_penguins[2] = tmp
            min_move += 1
        

    if copy_penguins[0] + 1 == copy_penguins[1] and copy_penguins[1] + 1 == copy_penguins[2]:
        break

print(min_move)
print(max_move)

if copy_penguins[0] + 1 == copy_penguins[1] and copy_penguins[1] + 1 == copy_penguins[2]:
    print(0)
    print(0)
    exit(0)

min_interval = 0

if penguins[1] - penguins[0] <= penguins[2] - penguins[1] and penguins[1] - penguins[0] != 1:
    min_interval = penguins[1] - penguins[0]
else:
    min_interval = penguins[2] - penguins[1]

min_move = min_interval // 2
max_move = min_move + 1


# --------------------------------------------------------

n, m = map(int, input().split())

robot_battle_dic = dict()

for _ in range(m):
    winner, loser = input().split()

    if winner in robot_battle_dic:
        robot_battle_dic.get(winner).append(loser)
    else:
        robot_battle_dic[winner] = [loser]


