
# ## 조합 반복문
# for i in range(8):
#     for j in range(i+1, 9):
#         for k in range(j+1, 10):
#             print(i, j, k)


## 재귀~~~~~~~~

def nCr(n, r, s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):  # n-r+k 선택할 수 있는 구간의 끝
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 10
R = 3
comb = [0] * R
nCr(N, R, 0, 0)