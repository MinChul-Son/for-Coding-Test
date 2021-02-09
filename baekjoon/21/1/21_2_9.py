# https://www.acmicpc.net/problem/2908
# a, b = input().split()
# a = list(a); b = list(b); a.reverse(); b.reverse(); a = int("".join(a)); b = int("".join(b))
# if a > b:
#     print(a)
# else:
#     print(b)

# https://www.acmicpc.net/problem/10809
# s = input()
# for i in range(97, 123):
#     if chr(i) in s:
#         print(s.index(chr(i)),end=" ")
#     else:
#         print(-1,end=" ")

# https://www.acmicpc.net/problem/11654
# print(ord(input()))

# https://www.acmicpc.net/problem/2675
# t = int(input())
# for _ in range(t):
#     r, s = input().split()
#     for i in s:
#         print(i*int(r),end="")
#     print("")

# https://www.acmicpc.net/problem/1157
# words = input().lower()
# words_list = list(set(words))
# word_count = list()

# for i in words_list:
#     count = words.count(i)
#     word_count.append(count)

# if(word_count.count(max(word_count)) >= 2):
#     print('?')
# else:
#     print(words_list[(word_count.index(max(word_count)))].upper())

# https://www.acmicpc.net/problem/5622
# s = input()
# sum = 0
# for i in s:
#     if i in 'ABC':
#         sum += 3
#     elif i in 'DEF':
#         sum += 4
#     elif i in 'GHI':
#         sum += 5
#     elif i in 'JKL':
#         sum += 6
#     elif i in 'MNO':
#         sum += 7
#     elif i in 'PQRS':
#         sum += 8
#     elif i in 'TUV':
#         sum += 9
#     else:
#         sum += 10
# print(sum)

# https://www.acmicpc.net/problem/11653
n = int(input())
if n == 1:
    pass
else:
    divide = 2
    while True:
        if n == 1:
            break
        if n % divide == 0:
            print(divide)
            n //= divide
            divide = 2
        else:
            divide += 1