import sys
input = sys.stdin.readline

## 유클리드 호제법
## 최소공배수 = (a * b) / 최대공약수

for tc in range(int(input())):
    tmp = list(map(int,input().split()))
    a, b = tmp[0], tmp[1]

    ## 우선, 최대공약수를 구해야 함
    while b > 0:
        a, b = b, a % b

    print(int(tmp[0]*tmp[1]/a))



## 시간초과 남

# for tc in range(int(input())):
#     tmp = list(map(int,input().split()))
#     tmp.sort()
#     a, b = tmp[0], tmp[1]
#
#     a *= b // a
#     while a != b:
#
#         if a < b:
#             a += tmp[0]
#
#         else:
#             b += tmp[1]
#
#     print(a)
