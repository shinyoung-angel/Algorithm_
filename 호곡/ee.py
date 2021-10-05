


def change (num):

    if original[num] == 1:
        original[num] = 0
    else:
        original[num] = 1


for tc in range(1, int(input())+1):
    N = int(input())
    led = list(map(int, input().split()))
    original = [0] * N
    cnt = 0


    for i in range(N):
        if led[i] != original[i]:
            num = i
            cnt += 1
            for j in range(num, N, num+1):
                change(j)
            if led == original:
                break

    print('#{} {}'.format(tc, cnt))