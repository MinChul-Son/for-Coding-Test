import sys
N = int(sys.stdin.readline())
play_list = list(map(int, sys.stdin.readline().split()))
Q = 0
reverse_list = []
if play_list == sorted(play_list):
    print(0)
else:
    for i in range(N):
        for j in range(N-1, i, -1):
            if play_list[j-1] >play_list[j]:
                play_list[j-1], play_list[j] = play_list[j], play_list[j-1]
                Q += 1
                reverse_list.append([play_list[j-1], play_list[j]])
        if Q > 100:
            print(-1)
            break
    else:
        print(Q)
        for i in range(Q-1, -1, -1):
            print(reverse_list[i][0], reverse_list[i][1])