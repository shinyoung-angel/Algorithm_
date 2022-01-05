

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)][::-1]
cnt = 0


for i in coin:
    if k >= i:
        cnt += k // i
        k %= i

    if k == 0:
        break

print(cnt)

