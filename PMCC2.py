import sys
N = int(sys.stdin.readline())
play_list = list(map(int, sys.stdin.readline().split()))
Q = 0
reverse_list = []

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if play_list[j] >play_list[j+1]:
            play_list[j], play_list[j+1] = play_list[j+1], play_list[j]
            Q += 1
            reverse_list.append([j+1, j+2])
        if Q > 100:
            print(-1)
            break
else:
    print(Q)
    for i,j in reverse_list:
        print(i,j)
