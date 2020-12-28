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
    elif minus ==0:
            continue
    else:
        count = count +(90-x+1)
print(count)