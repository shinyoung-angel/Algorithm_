
def dfs(x):

    visited[x] = 1

    for i in range(1, n+1):
        if arr[x][i] and not visited[i]:
            dfs(i)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        st, ed = map(int,input().split())
        arr[st][ed] = 1
        arr[ed][st] = 1

    cnt = 0
    for i in range(1, n+1):
        ###### 꼭 arr에 값이 있어야하진 않음!!!!!!!!!!!
        if not visited[i]:
            dfs(i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))