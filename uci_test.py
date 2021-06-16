dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    graph[x][y] = 'c'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                count += 1
                graph[nx][ny] = 'c'
                queue.append((nx, ny))
    return count


import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 입력 받기
for _ in range(t):
	num_cards = list(input().strip()) # 문자열로된 숫자카드를 리스트에 하나씩 담음
	num_cards.sort(reverse=True) # 리스트 내림차순 정렬
	answer = 0
	answer += int("".join(num_cards[:-1])) + int(num_cards[-1]) # 슬라이싱 사용
	print(answer) # 정답 출력
