import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

#### 나머지 분배 법칙을 알아야 함!!
#### (AxB)%C = (A%C) *(B%C) % C


def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))

#####
### 해당 계산 과정을 해결해주는 pow라는 함수도 있음
a,b,c= map(int, input().split())
print(pow(a,b,c))








###### 요것은 시간초과가 남

# progression = []
#
# for i in range(b+1):
#     tmp = a ** i % c
#     if tmp in progression:
#         break
#     else:
#         progression.append(tmp)
#
# print(progression[b%len(progression)])