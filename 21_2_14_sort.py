# # 이진 탐색 소스코드 구현 (재귀 함수)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid -1)
#     else:
#         return binary_search(array, target, mid + 1, end)

# # n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력 받기
# array = list(map(int, input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)




# 파이썬 이진 탐색 라이브러리
# from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4
# print(bisect_left(a,x))
# print(bisect_right(a,x))


# # 값이 특정 범위에 속하는 데이터 개수 구하기
# from bisect import bisect_left, bisect_right

# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# #배열 선언
# a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# # 값이 4인 데이터 개수 출력
# print(count_by_range(a, 4, 4))

# # 값이 [-1, 3] 범위에 있는 데이터 개수 출력
# print(count_by_range(a, -1, 3))


# # 떡볶이 떡 만들기 문제
# # 나의 풀이
# from bisect import bisect_left, bisect_right
# def cut_dduk(array, m, n):
#     max = 1
#     while True:
#         sum = 0
#         temp = 0
#         start = bisect_left(array,max)
#         for i in range(start, n):
#             temp = array[i] - max
#             if temp < 0:
#                 temp = 0
#             sum += temp
#         if sum < m:
#             break
#         max += 1
#     return max-1


# n, m = map(int, input().split())
# dduk = list(map(int, input().split()))
# dduk.sort()
# print(cut_dduk(dduk, m, n))

# # 답안 예시
# # 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
# n ,m = list(map(int, input().split(" ")))
# # 각 떡의 개별 높이 정보를 입력
# array = list(map(int, input().split()))

# #이진 탐색을 위한 시작점과 끝점 설정
# start = 0
# end = max(array)

# # 이진 탐색 수행 (반복적)
# result = 0
# while(start <= end):
#     total = 0
#     mid (start + end) // 2
#     for x in array:
#         # 잘랐을 때의 떡의 양 계산
#         if x > mid:
#             total += x - mid
#     # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
#     if total < m:
#         end = mid -1
#     # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
#     else:
#         result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
#         start = mid + 1

# #정답 출력
# print(result)


# # 정렬된 배열에서 특정 수의 개수 구하기 문제
# # 나의 풀이
# from bisect import bisect_left, bisect_right
# n, x = map(int, input().split())
# num_list = list(map(int, input().split()))
# if bisect_right(num_list,x)-bisect_left(num_list,x):
#     print(bisect_right(num_list,x)-bisect_left(num_list,x))
# else:
#     print(-1)


# # 답안 예시
# from bisect import bisect_left, bisect_right
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# count = count_by_range(array, x, x)
# if count == 0:
#     print(-1)
# else:
#     print(count)




