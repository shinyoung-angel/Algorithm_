
T = int(input())

for tc in range(1, T+ 1):
    L, P, C = map(int, input().split())
    cnt = 0
    while L * C < P:
        L = L * C
        cnt += 1
    ans = 0
    while cnt > 0:
        ans += 1
        cnt = cnt // 2
    print('#{} {}'.format(tc, ans))