import sys
input = sys.stdin.readline

## 처음했던 생각
## 처음 나오는 '-' 이후로는 모두 빼주면 되겠다! --> 땡!
## '-'가 나올 때마다 빼줘야 한다. 따라서 split으로 분리해야 함.

a = input()
## 자동으로 리스트 반환
num = a.split('-')


cnt = 0
for i in num[0].split('+'):     ## 리스트의 첫번째 요소를 cnt에 담아주기
    cnt += int(i)

for i in num[1:]:               ## 두번째 요소부터 다 빼주기
    num_piece = i.split('+')    ## 각 요소들은 더해줘야 함
    tmp = 0                     ## ex) 100 - (10+20) - (20+30) 요런 늑김
    for j in num_piece:
        tmp += int(j)
    cnt -= tmp

print(cnt)





## 이것은 런타임 에러 남!!

## 1. -를 기준으로 분리하기
a = input()
num = list(a.split('-'))

## 2. 첫번째 값 구하기
first = num[0]
cnt = 0
tmp = ''
for i in first:
    if i.isdigit():
        tmp += i
    else:
        cnt += int(tmp)
        tmp = ''
cnt += int(tmp)

## 3. 리스트 안의 요소들을 계산 후 다 빼주기
for i in num[1:]:
    tmp = ''
    tmp_add = 0
    for j in i:
        if j.isdigit():
            tmp += j
        else:
            tmp_add += int(tmp)
            tmp = ''
    tmp_add += int(tmp)
    cnt -= tmp_add

print(cnt)



