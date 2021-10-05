



N = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    r, c = map(int, input().split())

    for i in range(r, r+10):
        for j in range(c, c+10):

            arr[i][j] = 1
cnt = 0
for i in range(100):
    ##### 종이가 인접하지 않은 경우를 고려해줘야 함 !!!!!!! 오또케??????

    for j in range(99):
        if (arr[i][j] == 0 and arr[i][j+1] == 1) or (arr[j][i] == 0 and arr[j+1][i] == 1):
            cnt += 1
    for j in range(99, 0, -1):
        if (arr[i][j] == 1 and arr[i][j-1] == 0) or (arr[j][i] == 0 and arr[j-1][i] == 1):
            cnt += 1

print(cnt)

