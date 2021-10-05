
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

