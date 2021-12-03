

def dfs(cnt, value):
    global result


    if result >= value:
        return

    if cnt == n:
        result = value
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, value*arr[i][cnt]*0.01)
            visited[i] = 0



for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = -123456789
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, result*100))