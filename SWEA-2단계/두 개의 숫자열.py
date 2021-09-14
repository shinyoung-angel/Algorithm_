

# n이 m보다 큰 경우와, 작은 경우 모두 고려해야 함


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_value = 0

    if n > m:

        for i in range(n-m+1):
            ans = 0
            for j in range(m):
                ans += a[i+j] * b[j]
            if ans > max_value:
                max_value = ans

    else:

        for i in range(m-n+1):
            ans = 0
            for j in range(n):
                ans += a[j] * b[i+j]
            if ans > max_value:
                max_value = ans

    print('#{} {}'.format(tc, max_value))
