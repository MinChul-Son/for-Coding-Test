import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]
days = []
answer = []
for i in range(len(progresses)):
    x = math.ceil((100 - progresses[i])/speeds[i])
    days.append(x)

for i,d in enumerate(days):
    if i ==0:
        max = d
        answer.append(1)
        continue
    if d<=max:
        answer[-1] +=1
    else:
        max = d
        answer.append(1)
print(answer)