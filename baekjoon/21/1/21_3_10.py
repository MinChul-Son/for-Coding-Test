# https://www.acmicpc.net/problem/9184
import sys
sys.setrecursionlimit(10**6)
def solution(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return solution(20, 20, 20)
    elif a < b and b < c:
        return (solution(a, b, c-1) + solution(a, b-1, c-1) - solution(a, b-1, c))
    else:
        return (solution(a-1, b, c) + solution(a-1, b-1, c) + solution(a-1, b, c-1) - solution(a-1, b-1, c-1))
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w("+ str(a) + ", "+ str(b) + ", " + str(c) + ") = " + " " + str(solution(a,b,c)))
