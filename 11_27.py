from collections import Counter
def solution(source):
    dest = ''

    while source:
        tmp = Counter(source).items()
        tmp = sorted(tmp)
        new_source = ''
        for i in range(len(tmp)):
            dest += tmp[i][0]
            new_source += tmp[i][0] * (tmp[i][1] - 1)
        
        source = new_source
    return dest

# ------------------------------------------

def solution(r, c):
    answer = [[0] * c for _ in range(r)]
    
    

    return answer

#-------------------------------------------

def solution(grid):
    N = len(grid)

    for _ in range(N):
        for i in range(N):
            for j in range(N):
                tmp = []
                if grid[i][j] == 0:
                    continue

                if i+1 < N:
                    tmp.append(grid[i+1][j])

                if i-1 >= 0:
                    tmp.append(grid[i-1][j])

                if j+1 < N:
                    tmp.append(grid[i][j+1])

                if j-1 >= 0:
                    tmp.append(grid[i][j-1])

                grid[i][j] = min(tmp) + 1


    return max(map(max, grid))