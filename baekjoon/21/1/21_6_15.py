# https://www.acmicpc.net/problem/11058
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(101)]
dp[1] = 1; dp[2] = 2; dp[3] = 3; dp[4] = 4; dp[5] = 5; dp[6] = 6
for i in range(7, 101):
    dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)
print(dp[n])


#--------------------------------------------------------------------
# https://www.acmicpc.net/problem/3568
import sys
input = sys.stdin.readline

variables = list(input().split())
answer = []
for i in range(1, len(variables)):
    temp = variables[0]
    variable_name = ''
    variable_type = ''
    for i in variables[i][:-1]:
        if i.isalpha():
            variable_name += i
        else:
            variable_type += i
    variable_type = ''.join(list(reversed(variable_type)))
    if '][' in variable_type:
        variable_type = variable_type.replace('][','[]')
    temp += variable_type + ' ' + variable_name + ';'
    answer.append(temp)

for i in answer: print(i)
