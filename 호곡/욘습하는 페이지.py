
# import sys
#
# sys.stdin = open("i nput.txt", "r")



# N = 3
# arr = [1, 2, 3]
# sel = [0] * N  # 내가 직접 뽑은거 넣을 리스트
# check = [0] * N  # 내가 사용한거 체크할 리스트
#
#
# def perm(idx):
#     if idx == N:
#         print(sel)
#     else:
#         for i in range(N):
#             if check[i] == 0:
#                 sel[idx] = arr[i]
#                 check[i] = 1  # 사용했다... 쳌
#                 perm(idx + 1)
#                 check[i] = 0  # 원상복귀
#
# perm(0)

import itertools
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

operator_comb = set(list(itertools.permutations(operator, n-1)))



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
            num_sum = abs(num_sum) // num[j+1]
    result.add(num_sum)

print(max(result))
print(min(result))
