#### 생각보다 오래 생각했는데, 생각보다 매우 간단한 문제였다.
## 문자열을 이용!!

import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
result = 666

while True:

    if '666' in str(result):       ###666이 들어있나 진짜 하나한 검사
        cnt += 1

    if cnt == n:                    ## n번 돌면 끝
        break

    result += 1                     ## 아니면 값에다가 1씩 추가

print(result)
