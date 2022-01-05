# 그 곱한 아이들이 단조 증가하는 수인지 췤 췤
def check (yo):
    ans = list(str(yo))
    i = 0

    while i < len(ans) - 1:
        if ans[i] > ans[i+1]:
            return False
        i += 1
    return True


for tc in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    result = -1

    for i in range(N-1):
        for j in range(i+1, N):
            ans = num[i] * num[j]
            if result < ans and check(ans):
                result = ans


    print('#{} {}'.format(tc, result))



