
## 본인 숫자부터 쭈욱 나눠서 나눠지는 수가 2개 밖에 없다면 소수

n = int(input())
num = list(map(int, input().split()))
ans = 0

for i in num:

    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1

    if cnt == 2:
        ans += 1
    else:
        ans += 0


print(ans)