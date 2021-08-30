
# import sys
#
# sys.stdin = open("input.txt", "r")



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

for tc in range(1, int(input())+1):
    N = int(input())
    TC = list(map(int, input().split()))

    TC.sort()
    ans = []

    for i in range(5):
        ans.append(TC[-1-i])
        ans.append(TC[i])


    print('#{}'.format(tc), end= " ")
    for k in ans:
        print('{}'.format(k), end = " ")
    print()