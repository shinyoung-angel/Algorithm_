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
    for i in range(m):
        for i, tmp in enumerate(parties):
            if set.intersection(witness, tmp):
                witness.update(tmp)
                party_cnt[i] = 0


    print(sum(party_cnt)-1)







## 테스트케이스는 맞지만 틀림!

# n, m = map(int, input().split())
# true = list(map(int, input().split()))
# visited = [0] * (n+1)
# parties = [list(map(int, input().split())) for _ in range(m)]
#
# if true[0] != 0:
#     for i in true[1:]:
#         visited[i] = 1
#
#
# party_cnt = 0
#
# def check(party):
#
#     flag = True
#     for i in party:
#         if visited[i] == 1:
#             flag = False
#             break
#
#     if flag == False:
#         for j in party:
#             visited[j] = 1
#
#
# def check_2(party):
#
#     ans = 1
#     for i in party:
#         if visited[i] == 1:
#             ans = 0
#             break
#
#     return ans
#
#
# for i in range(m):
#     tmp = parties[i][1:]
#     check(tmp)
# for i in range(m):
#     tmp = parties[i][1:]
#     party_cnt += check_2(tmp)
#
# if true[0] == 0:
#     print(m)
# else:
#     print(party_cnt)
