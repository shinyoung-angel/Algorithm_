from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
operator_num = list(map(int, input().split()))
operator = ''
operator += '+'*operator_num[0]
operator += '-'*operator_num[1]
operator += '*'*operator_num[2]
operator += '/'*operator_num[3]
operator = list(operator)

operator_comb = set(list(permutations(operator)))

result = set()
for ope_set in operator_comb:
    num_sum = num[0]
    for j in range(n-1):
        if ope_set[j] == '+':
            num_sum += num[j+1]
        elif ope_set[j] == '-':
            num_sum -= num[j+1]
        elif ope_set[j] == '*':
            num_sum *= num[j+1]
        elif ope_set[j] == '/':
            ################### 조심 ###############
            if num_sum < 0:
                num_sum = abs(num_sum) // num[j + 1]
                num_sum *= -1
            else:
                num_sum = abs(num_sum) // num[j + 1]
    result.add(num_sum)

print(max(result))
print(min(result))

