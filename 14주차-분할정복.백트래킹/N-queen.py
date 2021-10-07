
def check(idx):
    global cnt

    if idx == n:
        cnt = 1
        return

    for i in range(n):
        if not visited[i]:
            row[idx] = i
            visited[i] = 1
            check(idx+1)
            visited[i] = 0



for tc in range(1, int(input())+1):
    n = int(input())
    visited = [0]* n
    row = [0] * n
    check(0)
    cnt = 0

    print('#{} {}'.format(tc, cnt))
