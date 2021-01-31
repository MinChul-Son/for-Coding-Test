# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            temp = stack.pop()
            if visited[temp] == 0:
                visited[temp] = 1
            for i in range(0, len(computers)):
                if computers[temp][i] == 1 and visited[i] ==0:
                    stack.append(i)
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer

