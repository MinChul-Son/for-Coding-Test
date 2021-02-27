# def main():
#     skill_list = input().split()
#     n = int(input())
#     chain_list = [input().split() for _ in range(n)]
#     answer = []
#     for i in chain_list:
#         for j in chain_list:
#             if i[1] == j[0]:
#                 answer.append([i[0], i[1], j[1]])  
#     for i in answer:    
#         print(*i)

# if __name__=="__main__":
#     main()


# def main():
#     p, n, h = map(int, input().split())
#     use_list = [list(map(int, input().split())) for _ in range(n)]
#     pc = [0 for _ in range(p+1)]
#     for i in use_list:
#         if i[1] > h:
#             continue
#         pc[i[0]] += i[1] * 1000
#     for i in range(1, p+1):
#         print(i, pc[i])


# if __name__=="__main__":
#     main()

# def main():
#     n = int(input())
#     step_list = list(map(int, input().split()))
#     visited = [0 for _ in range(n)]
#     answer = 0
#     for i in range(3):
#         temp_list = list(map(list, zip(step_list, visited)))
#         count = 1
#         current_location = i
#         while True:
#             if temp_list[current_location][1] == 1:
#                 break
#             count += 1
#             temp_list[current_location][1] = 1
#             current_location += temp_list[current_location][0]
#         if count > answer:
#             answer = count
#     print(answer)



# if __name__=="__main__":
#     main()


# def main():
#     n = int(input())
#     land_list = list(map(int, input().split()))
#     answer = 0
#     left = 0
#     right = n-1
#     while n != 1:
#         n //= 2 
#         max_left = max(land_list[left:left+n])
#         max_right = max(land_list[left+n:right+1])
#         if max_left > max_right:
#             answer += max_left
#             left += n
#         else:
#             answer += max_right
#             right -= n
#         print(answer)



# if __name__=="__main__":
#     main()






# select b.buyer_id, b.buy_date, a.book_name, a.price from library a join orderInfo b
# on a.book_id = b.book_id
# where a.book_name = "Looking with Elice" or b.buy_date between "2020-07-27" and "2020-07-31"
# order by b.buy_date;