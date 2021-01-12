#https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         if n % i ==0:
#             answer += i
#     return answer

#https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3

# def solution(num):
#     if num%2 ==0:
#         return 'Even'
#     else:
#         return 'Odd'

# https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3


# def solution(n):
#     n = list(map(int,list(str(n))))
#     return sum(n)


#https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

# def solution(phone_number):
#     phone_number = list(phone_number)
#     for i in range(0,len(phone_number)-4):
#         phone_number[i]='*'
#     return "".join(phone_number)


# https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3

# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     print('*'*a)


# https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

# def solution(num):
#     answer = 0
#     while num !=1:
#         if num%2 ==0:
#             num = num/2
#         else:
#             num = num*3 +1
#         answer +=1
#         if answer ==500:
#             return -1
        
#     return answer

# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

# def solution(x):
#     key = sum(list(map(int,list(str(x)))))
#     if x % key ==0:
#         return True
#     else:
#         return False


# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

# def solution(n):
#     answer = list(map(int,list(str(n))))
#     answer.reverse()
#     return answer

# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3

# def solution(x, n):
#     answer = []
#     temp = x
#     answer.append(x)
#     for i in range(1,n):
#         x +=temp
#         answer.append(x)
#     return answer


# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

# def solution(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)

# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


# def solution(arr):
#     arr.remove(min(arr))
#     if not arr:
#         arr.append(-1)
#         return arr
#     else:
#         return arr


# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         count = 0
#         temp_list = []
#         while count<len(arr1[0]):
#             temp_list.append(arr1[i][count]+arr2[i][count])
#             count +=1
#         answer.append(temp_list)
#     return answer

# https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

# def solution(n, m):
#     answer=[]
#     gcd_num = gcd(n,m)
#     lcm_num = lcm(n,m,gcd_num)
#     answer.append(gcd_num)
#     answer.append(lcm_num)
#     return answer
    
    
    
    
# def gcd(a, b):
#     if (b == 0):
#         return a
    
#     else:
#         return gcd(b, a%b)

# def lcm(a, b, g):
#     return g * (a/g) * (b/g)


#https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

# import math

# def solution(n):
#     if math.sqrt(n) == int(math.sqrt(n)):
#         return (math.sqrt(n)+1)*(math.sqrt(n)+1)
#     else:
#         return -1


#https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3

# def solution(n):
#     answer = list(str(n))
#     answer.sort(reverse=True)
#     return int("".join(answer))

# https://programmers.co.kr/learn/courses/30/lessons/12921

# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)

# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

# def solution(s):
#     charlist = []
#     for char in s.split(' ') :
#         idx = 0
#         for i in char:
#             if idx % 2 == 0:
#                 charlist.append(i.upper())
#             else :
#                 charlist.append(i.lower())
#             idx += 1
#         charlist.append(" ")

#     charlist.pop() 
#     #맨 마지막의 공백을 없애주기 위해 pop()

#     return "".join(charlist)