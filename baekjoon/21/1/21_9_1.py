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