# https://www.acmicpc.net/problem/14467
import sys
input = sys.stdin.readline

N = int(input())
cow_dic = dict()
answer = 0
for _ in range(N):
    cow_move = input().split()
    if cow_move[0] in cow_dic:
        if cow_dic[cow_move[0]] != cow_move[1]:
            answer += 1
            cow_dic[cow_move[0]] = cow_move[1]
            continue
    cow_dic[cow_move[0]] = cow_move[1]
print(answer)