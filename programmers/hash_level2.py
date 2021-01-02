# def solution(phone_book):
#     answer = True
    
#     for i in phone_book:
#         for j in range(len(phone_book)):
#             if i == phone_book[j][0:len(phone_book)]:
#                 answer = False
#                 return answer
        
#     return answer   

# phone_book = ['119', '97674223', '1195524421']

# answer = True
    
# for i in phone_book:
#     for j in range(len(phone_book)):
        
#         if phone_book.index(i)==j:
#                 continue
        
#         if i == phone_book[j][0:len(phone_book)]:
#             answer = False
#             return answer

# return answer
            
        
    

def solution(phone_book):
    answer = True
    
    for i in phone_book:
        for j in range(len(phone_book)):
            if i == phone_book[j][0:len(i)] and phone_book.index(i)!=j:
                    answer = False
                    return answer
            else:
                pass
        
    return answer    