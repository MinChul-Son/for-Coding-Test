import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for test_case in range(t):
        n = int(input())
        camel_times = list(map(int, input().split()))
        arrived_camel = []
        time = 0
        if len(camel_times) <= 2:
            print('#' + str(test_case+1) + ' %d' %max(camel_times))
            continue
        camel_times.sort()
        arrived_camel.extend(camel_times[:2])
        time += max(camel_times[:2])
        del camel_times[:2]
        while camel_times:
            comeback_camel = min(arrived_camel)
            time += comeback_camel
            camel_times.append(comeback_camel)
            arrived_camel.remove(comeback_camel)
            camel_times.sort()
            start_camel = camel_times[-2:]
            arrived_camel.extend(start_camel)
            time += max(start_camel)
            del camel_times[-2:]
        print('#' + str(test_case+1) + ' %d' %time)
main()

#----------------------------------------------------------
def main():
    
    
main()


#-------------------------------------------------------
import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for test_case in range(t):
        n, k = map(int, input().split())
        graph = [list(input().strip()) for _ in range(k)]
        move_list = []
        for standard_row in range(k):
            move = 0
            for ring in range(n):
                temp_move = 0 # 1이 2개 이상 존재하는 ring을 위한 변수
                if graph[standard_row][ring] == '1':
                    continue
                for column in range(k):
                    if graph[column][ring] == '1':
                        if temp_move == 0:
                            temp_move = min(abs(standard_row-column), (standard_row+k-column))
                        else:
                            temp_move = min(abs(standard_row-column), (standard_row+k-column), temp_move)
                move += temp_move
            move_list.append(move)
        print('#' + str(test_case+1) + ' %d' %min(move_list))

main()