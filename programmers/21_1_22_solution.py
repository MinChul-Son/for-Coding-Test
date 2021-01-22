# def solution(name):
#     sample = []
#     temp=[]
#     temp=name
#     count = -1
#     for i in temp:
#         sample.append('A')
#     for i in range(0, len(temp)):      
#         count +=1
#         x= ord(temp[i])
#         y= ord(sample[i])
#         minus= x - y
#         move = 0
#         if minus <13:
#             count= count +minus
#         else:
#             count = count +(90-x+1)
#     for i in range(0, len(temp)):
#         if temp[i]=='A':
#             count = count -1
            
#     return count

# def solution(name):
#     make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
#     idx, answer = 0, 0
#     while True:
#         answer += make_name[idx]
#         make_name[idx] = 0
#         if sum(make_name) ==0:
#             break
#         left, right = 1, 1
#         while make_name[idx - left] ==0:
#             left +=1
#         while make_name[idx + right] ==0:
#             right +=1
#         answer += left if left < right else right
#         idx += -left if left < right else right
#     return answer