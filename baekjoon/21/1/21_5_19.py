# https://www.acmicpc.net/problem/14500
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
tetrominoes = [
    # 긴거
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # 네모난거
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # ㄴ 모양
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # 번개 모양
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [-1, 0], [-1, 1], [-2, 1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # ㅗ 모양
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, -1]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]]
]
for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            # 블록이 종이 안에 들어오는 지 확인하기
            for k in range(4):
                if not (0 <= (i + tetromino[k][0]) < n and 0 <= (j + tetromino[k][1]) < m):
                    break
            # 블록이 종이 안에 들어오면 값 계산하기
            else:
                temp = 0
                for k in range(4):
                    temp += graph[i + tetromino[k][0]][j + tetromino[k][1]]
                max_num = max(temp, max_num)
print(max_num)