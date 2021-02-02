# def solution(n):
#     a,b = 0, 1
#     for i in range(n):
#         a,b = b, a+b
#     return a % 1234567


def solution(arr):
    answer = []
    if len(arr) == 1:
        return [arr.count(0),arr.count(1)]
    elif len(arr) == 2:
        if (arr[0].count(0)+arr[1].count(0)) == 4 or (arr[0].count(1)+arr[1].count(1)) == 4:
    return answer

print(solution([1]))