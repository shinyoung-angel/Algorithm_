import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt_0 = 0
cnt_1 = 0
cnt_minus = 0


def check(x, y, n):
    global cnt_0, cnt_1, cnt_minus

    tmp = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != tmp:
                for k in range(3):
                    for h in range(3):
                        check(x+k*n//3, y+h*n//3, n//3)
                return


    if tmp == 0: cnt_0 += 1
    elif tmp == -1: cnt_minus += 1
    else: cnt_1 += 1


check(0,0,n)
print(cnt_minus)
print(cnt_0)
print(cnt_1)