# def solution(code, day, data):
#     answer = []
#     for i in range(len(data)):
#         data[i] = data[i].split(" ")
#     data = sorted(data, key=lambda x: int(x[2][5:]))

#     for i in range(len(data)):
#         if data[i][1][5:] == code and data[i][2][5:-2] == day:
#             answer.append(int(data[i][0][6:]))
#     return answer


#------------------------------------------------------------------
import heapq
def solution(t, r):
    answer = []
    queue = []
    for i in range(len(t)):
        queue.append((t[i], r[i], i))
    queue = sorted(queue, key=lambda x: (x[0], x[1], x[2]))
    count = 0
    for i in range(max(t)):
        heap = []
        for j in queue:
            if not queue:
                break
            if i >= j[0]:
                heapq.heappush(heap, (j[1], j[2]))
                queue.remove(j)
        else:
            if heap:
                answer.append(heap[0][1])
            continue
        break
    answer.append(queue[0][2])
    return answer

solution([7,6,8,1], [0,1,2,3])