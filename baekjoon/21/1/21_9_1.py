# https://www.acmicpc.net/problem/10799
import sys

input = sys.stdin.readline().strip()
answer = 0
stack = []
for i,p in enumerate(input):
    if p == '(':
        stack.append(p)
        continue
    
    stack.pop()

    if input[i-1] == '(':
        answer += len(stack)
    else:
        answer += 1

print(answer)

# https://www.acmicpc.net/problem/2346
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))
answer = [1]

for i in range(len(balloons)):
    balloons[i] = (balloons[i], i+1)

move = balloons[0][0]
position = 0
balloons.pop(0)

for _ in range(N-1):
    if move < 0:
        position = (position + move) % len(balloons)
    else:
        position = (position + move - 1) % len(balloons)
    
    temp = balloons.pop(position)
    move = temp[0]
    answer.append(temp[1])

print(*answer)