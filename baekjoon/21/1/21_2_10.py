while True:
    m = int(input())
    if m == 0:
        break
    elif m == 1:
        print(1)
    else:
        n = 2*m 
        count = 0
        num_list = [True for _ in range(n)]
        for i in range(2, int(n**0.5) + 1):
            if num_list[i] == True:
                for j in range(2*i, n, i):
                    num_list[j] = False
        for i in range(m+1, n):
            if i >1 and num_list[i] == True:
                count += 1
        print(count)