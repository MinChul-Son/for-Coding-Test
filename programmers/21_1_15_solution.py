# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3


# def solution(n):
#     answer = 0
#     conver_list = list(convert(n))
#     #conver_list.reverse()
#     for i in range(len(conver_list)):
#         answer += ((3**i)*int(conver_list[i]))
#     return answer



# def convert(n):
#     T = "0123456789ABCDEF"
#     q, r = divmod(n, 3)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q) + T[r]



# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += (a[i]* b[i])
#     return answer


# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# from itertools import product

# def solution(numbers, target):
#     all_list = [(x,-x) for x in numbers]
#     s =list(map(sum,product(*all_list)))
#     return s.count(target)



# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

# def solution(citations):
#     citations.sort()
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
#             return l-i
#     return 0

# https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3
# def solution(s):
#     s = list(s)
#     if s[0] == ')' or s[-1] == '(':
#         return False

#     if s.count('(') == s.count(')'):
#         count_open = 0
#         for i in s:
#             if i == '(':
#                 count_open += 1
#             else:
#                 count_open -= 1
#             if count_open<0:
#                 return False 
#         return True
#     else:
#         return False




# https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3

# def solution(num):
#     a,b = 0,1
#     for i in range(num):
#         a,b = b,a+b
#     return a %1234567


# https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3

# def solution(s):
#     split_list = list(map(int,list(s.split(" "))))
#     return str(min(split_list)) + " "+ str(max(split_list))


# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
# from itertools import combinations

# def solution(number, k):
#     answer = 0
#     removed = len(number)-k
#     number = list(number)
#     all_list = list(combinations(number,removed))
#     for i in all_list:
#         if answer < int("".join(i)):
#             answer = int("".join(i))
#     return str(answer)  

#==> 다른사람 풀이
# def solution(number, k):
#     # stack에 입력값을 순서대로 삽입 
#     stack = [number[0]]
#     for num in number[1:]:
#         # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
#         # 참고 : len(stack) > 0 == stack
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             # 값을 한개 빼서 k는 1이 제거 
#             k -= 1
#             # 내부의 값을 제거 
#             stack.pop()
#         # 새로운 값을 삽입 
#         stack.append(num)
#     # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
#     # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)



# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

# def solution(n):
#     start_num = n
#     count_one = list(str(format(n,'b'))).count('1')
#     answer = 0
#     while True:
#         start_num += 1
#         count_new = list(str(format(start_num,'b'))).count('1')
#         if count_one == count_new:
#             return start_num


# https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3
# def solution(A,B):
#     A.sort()
#     B.sort(reverse=True)
#     answer = 0
#     for i in range(len(A)):
#         answer += A[i] * B[i]


#     return answer
