import sys
input = sys.stdin.readline


## 팩토리얼 숫자 구하기
def fact(n):

    if n <= 1: return 1
    else: return n * fact(n-1)

num = int(input())
fact_num = str(fact(num))
fact_len = len(fact_num)

## 뒤에서부터 0을 카운트 하기
cnt = 0
for i in range(fact_len-1, -1, -1):
    tmp = fact_num[i]
    if tmp == '0': cnt += 1  ## 0이면 카운트, 아니라면 break
print(cnt)


