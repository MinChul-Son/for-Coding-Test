# # https://www.acmicpc.net/problem/3085
N = int(input())
candies = ['0' for x in range(N)]
for i in range(N):
    candies[i] = [x for x in input()]

def count_candy(x,y):
    row_count = 0
    col_count = 0
    max_count = 0
    row_start = candies[0][y]
    col_start = candies[x][0]
    for i in range(N):
        if candies[i][y]==row_start:
            row_count += 1
            if max_count < row_count:
                max_count = row_count
        else:
            row_start = candies[i][y]
            row_count = 1

        if candies[x][i]==col_start:
            col_count += 1
            if max_count < col_count:
                max_count = col_count
        else:
            col_start = candies[x][i]
            col_count = 1
    return max_count


def change_candy(x1, y1, x2, y2):
    temp = candies[x1][y1]
    candies[x1][y1] = candies[x2][y2]
    candies[x2][y2] = temp

max_count = list()
for i in range(N):
    for j in range(N):
        # Right
        if j<N-1:
            change_candy(i,j, i, j+1)
            max_count.append(count_candy(i,j))
            max_count.append(count_candy(i, j+1))
            change_candy(i, j+1, i, j)
        # Down
        if i<N-1:
            change_candy(i,j, i+1, j)
            max_count.append(count_candy(i, j))
            max_count.append(count_candy(i+1, j))
            change_candy(i + 1, j, i, j)

print(max(max_count))

#-----------------------------------------------------------------
# https://www.acmicpc.net/problem/1038
import sys
input = sys.stdin.readline
n = int(input())
def solve(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1
if n >= 1023:  # 1022: 9876543210
    print(-1)  # N번째 감소하는 수 x
elif n == 0:
    print(0)
else:
    print(solve(n))
