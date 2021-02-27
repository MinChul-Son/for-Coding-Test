# https://www.acmicpc.net/problem/2841
import sys
n, p = map(int, sys.stdin.readline().split())
melody_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
stack = [[] for _ in range (7)]
move = 0
for i,j in melody_list:
    if not stack[i]:
        stack.append(j)
        move += 1
        continue
    if j > stack[i][-1]:
        stack.append(j)
        move += 1
    elif j == stack[i][-1]:
        continue
    else:
        while len(stack[i]) != 0 and j < stack[i][-1]:
            stack[i].pop()
            move += 1
        if len(stack[i]) != 0 and j == stack[i][-1]:
            continue
        stack[i].append(j)
        move += 1
print(move)
