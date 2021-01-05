import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7 
count = 0
heap = []
for i in scoville:
    heapq.heappush(heap, i)
while heap[0]<K:
    if len(heap)==1:
        break   
    heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
    count +=1


#답
# import heapq

# def solution(scoville, K):
#     count = 0
#     heap = []
#     for i in scoville:
#         heapq.heappush(heap, i)
#     while heap[0]<K:
#         if len(heap)==1:
#             return -1
        
#         heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
#         count +=1
#     return count
