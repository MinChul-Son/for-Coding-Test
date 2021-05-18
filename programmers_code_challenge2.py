# def solution(left, right):
#     answer = 0
#     for i in range(left, right+1):
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#         if count % 2 == 0:
#             answer += i
#         else:
#             answer -= i
#     return answer


#-----------------------------------------------------------------------------
# def solution(numbers):
#     answer = []
#     for i in numbers:
#         bit_list = [0 for _ in range(50)]
#         temp = list(format(i, 'b'))
#         temp.reverse()
#         for j, bit in enumerate(temp):
#             bit_list[j] = bit
#         compare_num = i
#         while True:
#             count = 0
#             compare_num += 1
#             compare_list = [0 for _ in range(50)]
#             temp = list(format(compare_num, 'b'))
#             temp.reverse()
#             for j, bit in enumerate(temp):
#                 compare_list[j] = bit
#             for j in range(50):
#                 if bit_list[j] != compare_list[j]:
#                     count +=1
#                 if count > 2:
#                     break
#             else:
#                 answer.append(compare_num)
#                 break 


#     print(answer)     
#     return answer


# def solution(numbers):
#     answer = []
#     for i in numbers:
#         bit_list = list(format(i, 'b'))
#         compare_num = i
#         while True:
#             count = 0
#             compare_num += 1
#             compare_bit_list = list(format(compare_num, 'b'))

#             if len(compare_bit_list) > len(bit_list):
#                 bit_list = list("0" * (len(compare_bit_list) - len(bit_list)) + "".join(bit_list))
#             else:
#                 compare_bit_list = list("0" * (len(bit_list) - len(compare_bit_list)) + "".join(compare_bit_list))

#             for j in range(len(bit_list)-1, -1, -1):
#                     if bit_list[j] != compare_bit_list[j]:
#                         count += 1
#                     if count > 2:
#                         break
#             else:
#                 answer.append(compare_num)
#                 break        
#     print(answer)
#     return answer

def solution(numbers):
    answer = []
    for i in numbers:
        bit_list = list(format(i, 'b'))
        compare_num = i
        while True:
            count = 0
            compare_num += 1
            compare_bit_list = list(format(compare_num, 'b'))

            count += len(compare_bit_list) - len(bit_list)
            compare_bit_list = compare_bit_list[-len(bit_list):]
            for j in range(len(bit_list)):
                if bit_list[j] != compare_bit_list[j]:
                        count += 1
            if count <= 2:
                break
        answer.append(compare_num)
    return answer
solution([2,7])