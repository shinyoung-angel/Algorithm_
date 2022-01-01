
def possible(idx, cnt):
    global chance

    if chance >= cnt:
        return

    if idx == n:
        chance = cnt
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            possible(idx+1, cnt*arr[i][idx]*0.01)
            visited[i] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    chance = -123456
    possible(0, 1)

    print('#{} {:.6f}'.format(tc, chance*100))


