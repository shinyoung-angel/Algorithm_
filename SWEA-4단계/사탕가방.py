

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    candies = list(map(int, input().split()))
    result = 0

    if sum(candies) < m:
        break
    else:



    print('#{} {}'.format(tc, result))

##

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    low = 1
    high = max(A)
    while low <= high:
        mid = (low+high)//2
        total = 0
        for e in A:
            total += e//mid
        if total < M:
            high = mid - 1
        else:
            low = mid + 1
    print("#", test_case, " ", high, sep='')