# #Codeup Basic-100 with Python

# #1001
# print("Hello")

# #1002
# print("Hello World")

# #1003
# print("Hello\nWorld")

# #1004
# print("'Hello'")

# #1005
# print('"Hello World"')

# #1006
# print('"!@#$%^&*()"')

# #1007
# print('"C:\Download\hello.cpp"')

# #1008
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# print('\u250C\u252C\u2510')
# print("\u251C\u253C\u2524")
# print("\u2514\u2534\u2518")

# #1010
# a=input()
# a=int(a)
# print(a)

# #1011
# a = input()
# print(a)

# #1012
# a=input()
# a=float(a)
# print("%f" % a)

# #1013
# a, b = input().split()
# print(a, b)

# #1014
# a,b = input().split() # 각각의 입력값이 공백으로 구분되어 있다는 뜻
# print(b,a)

# #1015
# a = float(input())
# print("%.2f" % a) #("%.2" % a) 는 a의 값을 소숫점 셋 째 자리에서 반올림 한 값을 나타냄

# #1017
# a = input()
# print(a, a, a)

# #1018
# a ,b = input().split(":")
# print(a+":"+b)

# #1019
# a ,b, c = input().split(".")
# print("%04d.%02d.%02d" %(int(a),int(b),int(c)))

# #1020
# a ,b = input().split("-")
# print("%06d%07d" %(int(a),int(b)))

# #1021
# a=input()
# print(a)

# #1022
# a=input()
# print(a)

# #1023
# a,b=input().split(".")
# print(a,end="\n")
# print(b)

# #1024
# a=input()
# for i in a:
#     print("'"+i+"'")

# #1025
# a=input()
# print("[%d]" %(int(a[0])*10000))
# print("[%d]" %(int(a[1])*1000))
# print("[%d]" %(int(a[2])*100))
# print("[%d]" %(int(a[3])*10))
# print("[%d]" %(int(a[4])))

# #1026
# a,b,c=input().split(":")
# print(int(b))

# #1027
# a,b,c=input().split(".")
# print("%02d-%02d-%04d" %(int(c),int(b),int(a)))

# #1028
# a=input()
# print(a)

# #1029
# a=input()
# print("%.11f" %(float(a)))

# #1030
# a=input()
# print(a)

# #1031
# a=int(input())
# print("%o" %a) #%o는 8진수로 출력

# #1032
# a=int(input())
# print("%x" %a) #%x로 출력하면 16진수 소문자

# #1033
# a=int(input())
# print("%X" %a)#%x로 출력하면 16진수 대문자

# #1034
# a=input()
# print(int(a,8)) #8진수로 입력된 정수 1개를 10진수로 바꾸어 출력

# #1035
# a=int(input(),16)
# print("%o" %a)#16진수로 입력된 정수 1개를 8진수로 바꾸어 출력

# #1036
# a=ord(input()) #ord는 문자의 아스키 코드 값을 돌려주는 함수
# print(a)

# #1037
# a=chr(int(input())) #chr함수는 정수를 아스키 코드값으로 매칭시켜 문자열로 변환
# print(a)

# #1038
# a,b=input().split()
# print(int(a)+int(b))

# #1039
# a,b=input().split()
# print(int(a)+int(b))

# #1040
# a=int(input())
# print(-a)

# #1041
# a=chr(ord(input())+1)
# print(a)

# #1042
# a,b=input().split(" ")
# print(int(a)//int(b))

# #1043
# a,b=input().split(" ")
# print(int(a)%int(b))

# #1044
# a=input()
# print(int(a)+1)

# #1045
# a,b=input().split(" ")
# print(int(a)+int(b))
# print(int(a)-int(b))
# print(int(a)*int(b))
# print(int(a)//int(b))
# print(int(a)%int(b))
# print("%.2f" %(int(a)/int(b)))

# #1046
# a,b,c=input().split(" ")
# sum = int(a)+int(b)+int(c)
# print(sum)
# print("%.1f" %(sum/3))

# #1047 비트시프트 연산
# a = int(input())
# print(a<<1) #a*2랑 같은 값 반대로 a>>1은 a/2

# #1048
# a,b = input().split(" ")
# print(int(a)<<int(b)) #a<<b는 a에 2의 b승배를 곱하는 것

# #1049
# a,b = input().split(" ")
# if int(a)>int(b):
#     print(1)
# else:
#     print(0)

# #1050
# a,b = input().split(" ")
# if int(a)==int(b):
#     print(1)
# else:
#     print(0)

# #1051
# a,b = input().split(" ")
# if int(a)>int(b):
#     print(0)
# else:
#     print(1)

# #1052
# a,b = input().split(" ")
# if int(a)!=int(b):
#     print(1)
# else:
#     print(0)

# #1053
# a = int(input())
# if a ==1:
#     print(0)
# else:
#     print(1)

# #1054
# a,b = input().split(" ")
# if int(a)==1 and int(b)==1:
#     print(1)
# else:
#     print(0)

# #1055
# a,b = input().split(" ")
# if int(a)==1 or int(b)==1:
#     print(1)
# else:
#     print(0)

# #1056
# a,b = input().split(" ")
# if int(a)!=int(b):
#     print(1)
# else:
#     print(0)

# #1057
# a,b = input().split(" ")
# if int(a)==int(b):
#     print(1)
# else:
#     print(0)

# #1058
# a,b = input().split(" ")
# if int(a)==0 and int(b)==0:
#     print(1)
# else:
#     print(0)

# #1059
# a = int(input())
# print("%d" %~a)

# #1060
# a,b = input().split(" ")
# print(int(a)&int(b))

# #1061
# a,b = input().split(" ")
# print(int(a)|int(b))

# #1062
# a,b = input().split(" ")
# print(int(a)^int(b))

# #1063
# a,b = input().split(" ")
# print(a if int(a)>int(b) else b) #파이썬에는 ?같은 삼항 연산자 대신 왼쪽처럼 사용

# #1064
# a,b,c = input().split(" ")
# print(min(int(a),int(b),int(c)))

# #1065
# a,b,c = input().split(" ")
# if int(a)%2 ==0:
#     print(a)
# if int(b)%2 ==0:
#     print(b)
# if int(c)%2 ==0:
#     print(c)

# #1066
# a = input().split(" ")
# for i in a:
#     if int(i)%2 ==0:
#         print("even")
#     else:
#         print("odd")

# #1067
# a = int(input())
# if a >0:
#     print("plus")
# else:
#     print("minus")
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# #1068
# a = int(input())
# if a>=90:
#     print("A")
# elif a>=70:
#     print("B")
# elif a>=40:
#     print("C")
# else:
#     print("D")

# #1069
# a = input()
# if a =='A':
#     print("best!!!")
# elif a=='B':
#     print("good!!")
# elif a=='C':
#     print("run!")
# elif a=='D':
#     print("slowly~")
# else:
#     print("what?")

# #1070
# a= int(input())
# if a==12 or a==1 or a==2:
#     print("winter")
# elif a==3 or a==4 or a==5:
#     print("spring")
# elif a==6 or a==7 or a==8:
#     print("summer")
# else:
#     print("fall")

# #1071
# a = input().split()
# for x in a :
#     if int(x)==0 :
#         break
#     else :
#         print(x)

# #1072
# a = int(input())
# b = input().split()
# c = map(int, b)
# for x in c :
#     print(x)

# #1073
# a = input().split()
# for x in a :
#     if int(x)==0 :
#         break
#     else :
#         print(x)

# #1074
# a = int(input())
# while a!=0:
#     print(a)
#     a-=1

# #1075
# a = int(input())
# while a>0:
#     a-=1
#     print(a)

# #1076
# a = ord(input())
# b = ord('a')
# while a>=b :
#     print(chr(b),end = ' ')
#     b=b+1  

# #1077
# a = int(input())
# b =0
# while b<=a:
#     print(b)
#     b+=1

# #1078
# a = int(input())
# b =1
# sum =0
# while b<=a:
#     if b%2==0:
#         sum+=b
#     b+=1
# print(sum)

# #1079
# a = input().split()
# for i in a :
#     print(i)
#     if i == 'q':
#         break

# #1080
# a = int(input())
# sum =0
# for i in range(1,a+1):
#     sum +=i
#     if sum>=a:
#         print(i)
#         break

# #1081
# a, b = input().split(" ")
# for i in range(1,int(a)+1):
#     for j in range(1, int(b)+1):
#         print(i, end=" ")
#         print(j)

# #1083
# a = int(input())
# for i in range(1, a+1):
#     if i%3==0:
#         print("X")
#     else:
#         print(i)

# #1084
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = 0
# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             print(i,j,k)
#             d+=1
# print(d)

# #1085
# a, b, c, d = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# result =float(a*b*c*d/8/1024/1024)
# print("%.1f" %result, end=" ")
# print("MB")

# #1086
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# result = float(a*b*c/8/1024/1024)
# print("%.2f MB" %result)

# #1087
# a = int(input())
# sum =0
# for i in range(1,a+1):
#     sum +=i
#     if sum>=a:
#         print(sum)
#         break

# #1088
# a = int(input())
# for i in range(1, a+1):
#     if i%3==0:
#         pass
#     else:
#         print(i, end=" ")

# #1089
# a, d, n =input().split()
# a= int(a)
# d= int(d)
# n = int(n)
# for i in range (1, n):
#     a+=d
# print(a)

# #1090
# a, d, n =input().split()
# a= int(a)
# d= int(d)
# n = int(n)
# for i in range (1, n):
#     a*=d
# print(a)

# #1091
# a, m, d, n =input().split()
# a= int(a)
# m = int(m)
# d= int(d)
# n = int(n)
# for i in range (1, n):
#     a=a*m+d
# print(a)

# #1092
# a, d, n =input().split()
# a= int(a)
# d= int(d)
# n = int(n)
# i = 1
# while (i%a!=0 or i%d!=0 or i%n!=0):
#     i+=1
# print(i)



# #1093
# a = int(input())
# b=input().split()
# list=[]
# for i in range(24):
#     list.append(0)
# for i in range(a):
#     list[int(b[i])] +=1
# for i in range(1,24):
#     print(list[i], end=" ")

# #1094
# a = int(input())
# b=input().split()
# b.reverse() #list순서 거꾸로 뒤집기
# for i in range(0,a):
#     print(b[i], end=" ")

#1095
a = int(input())
b=input().split()
b.sort()
print(b[0])

#1096
m=[]
for i in range(20) :
    m.append([]) 
    for j in range(20) :
        m[i].append(0) 

n=int(input()) 
for i in range(n) :
    x,y=input().split() 
    m[int(x)][int(y)]=1 

for i in range(1, 20) : 
    for j in range(1, 20) : 
        print(m[i][j], end=' ') 
    print()

