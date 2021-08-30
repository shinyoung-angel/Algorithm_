
check = [[0]*100 for _ in range(100)]


for _ in range(int(input())):
    c, r = map(int, input().split())

    for i in range(r, r+10):
        for j in range(c, c+10):
            check[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if check[i][j] == 1:
            ans += 1

print(ans)