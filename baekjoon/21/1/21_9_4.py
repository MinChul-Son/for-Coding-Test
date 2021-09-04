# https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline

n = int(input())
rest = n%5

if n == 1 or n == 3:
    print(-1)
elif rest % 2 == 0:
    print(n // 5 + rest // 2)
else:
    print((n // 5) -1 + (rest + 5) // 2)

# https://www.acmicpc.net/problem/1343
import sys
input = sys.stdin.readline

board = input().strip()
board = board.replace("XXXX", "AAAA") 
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
else:
    print(board)
