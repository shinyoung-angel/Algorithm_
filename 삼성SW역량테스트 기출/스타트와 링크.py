from itertools import combinations as comb
import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

comb_list = list(comb(list(range(n)), n//2))        ## 두 조합으로 나누기
comb_cnt = len(comb_list)
result = 123456789

for team in range(comb_cnt//2):                     ## 팀 하나를 뽑아 다시 조합 만들기
    a_comb = list(comb(comb_list[team], 2))
    b_comb = list(comb(comb_list[-team-1], 2))

    a = b = 0
    for persons in a_comb:
        a += arr[persons[0]][persons[1]] + arr[persons[1]][persons[0]]

    for persons in b_comb:
        b += arr[persons[0]][persons[1]] + arr[persons[1]][persons[0]]

    extract = abs(a-b)
    result = min(result, extract)

print(result)


