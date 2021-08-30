

for tc in range(1, int(input())+1):
    N = int(input())
    TC = list(input().split())
    mid = N//2
    result = []

    if N % 2:
        a = TC[:mid+1]
        b = TC[mid+1:]
        try:
            for i in range(mid+1):
                result.append(a[i])
                result.append(b[i])

        except:
            pass

    if N % 2 == 0:
        a = TC[:mid]
        b = TC[mid:]
        for i in range(mid):
            result.append(a[i])
            result.append(b[i])
    result = ' '.join(result)
    print('#{} {}'.format(tc, result))