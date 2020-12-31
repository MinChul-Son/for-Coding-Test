name ="JAN"
temp =[]
temp = name
sample = []
count = -1
for i in temp:
        sample.append('A')
for i in range(0, len(temp)):
    print(count)
    count +=1
    x= ord(temp[i])
    y= ord(sample[i])
    print(x,y)
    minus= x - y
    move = 0
    if minus <13:
        count= count +minus
    
    else:
        count = count +(90-x+1)
print(count)




# def solution(name):
#     sample = []
#     temp=[]
#     temp=name
#     count = -1
#     move = 0
#     for i in temp:
#         sample.append('A')
#     for i in range(0, len(temp)):
#         x= ord(temp[i])
#         y= ord(sample[i])
#         minus= x - y
#         if minus <13:
#             count= count +minus
#         else:
#             count = count +(90-x+1)
#     for i in range(0, len(temp)):
#         if temp[i] != 'A':
#             continue
#         else:
#             move+=1
#     right = len(temp)-1
#     if move != 0:
#         count = count +right -move
#     else:
#         count + right
    
#     return count