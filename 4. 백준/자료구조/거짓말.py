import sys
input = sys.stdin.readline

### 파이썬의 intersection, union 함수 사용 !!

n, m = map(int, input().split())
witness_list = list(map(int, input().split()))
witness = set(witness_list[1:])
parties = [list(map(int, input().split()))[1:] for _ in range(m)]
party_cnt = [1] * (m+1)

if witness_list[0] == 0:
    print(m)
else:
    for i in range(m):  ########### 주의 ~~~~~~~~~!!!!
        for i, tmp in enumerate(parties):
            if set.intersection(witness, tmp):
                witness.update(tmp)
                party_cnt[i] = 0


    print(sum(party_cnt)-1)


# 테스트케이스는 맞지만 틀림! --> 맞음!!!!!!!!!!
####

n, m = map(int, input().split())
true = list(map(int, input().split()))
visited = [0] * (n+1)
parties = [list(map(int, input().split())) for _ in range(m)]

if true[0] != 0:
    for i in true[1:]:
        visited[i] = 1


party_cnt = 0

def check(party):
    ans = 1
    flag = True
    for i in party:
        if visited[i] == 1:
            ans = 0
            flag = False
            break

    if flag == False:
        for j in party:
            visited[j] = 1

    return ans


### 반례를 생각해봤어야 했다!!
## ex, 5,6 // 4,5 // 3,4 // 2,3 // 1,2 ==> 5개의 파티를 총 5번 돌아야함!!! 즉 25번 췤 필요
for j in range(m):  ##### 요기 한 줄  수정 후 정답!!! 파티 갯수만큼 쳌해줘야 했ㅇ음!!
    for i in range(m):
        tmp = parties[i][1:]
        check(tmp)
for i in range(m):
    tmp = parties[i][1:]
    party_cnt += check(tmp)

if true[0] == 0:
    print(m)
else:
    print(party_cnt)
