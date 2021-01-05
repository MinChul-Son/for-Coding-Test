priorities = [1, 1, 9, 1, 1, 1]
location = 0
temp = priorities[location]
temp_length = len(priorities)
temp_list = []
out = [] #나온 순서
for i,p in enumerate(priorities):
    temp_list.append(i)
temp_list = list(zip(priorities,temp_list))

while len(out) < temp_length:
    if max(temp_list)[0] == temp_list[0][0]:
        out.append(temp_list.pop(0))
    else:
        temp_list.append(temp_list.pop(0))

print(out.index((temp,location))+1)