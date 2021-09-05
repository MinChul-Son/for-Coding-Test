# https://www.acmicpc.net/problem/20291
import sys
input = sys.stdin.readline

N = int(input())
file_dic = dict()
for _ in range(N):
    file = input().strip().split('.')
    if file[1] in file_dic:
        file_dic[file[1]] += 1
    else:
        file_dic[file[1]] = 1

answer = sorted(file_dic.items())
for i in answer:
    print(*i)

# https://www.acmicpc.net/problem/16171
import sys
input = sys.stdin.readline

S = input().strip()
K = input().strip()

remove_numeric = ""

for i in S:
    if i.isalpha():
        remove_numeric += i

if K in remove_numeric:
    print(1)
else:
    print(0)