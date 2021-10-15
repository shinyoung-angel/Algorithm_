
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


##############

def make_set(x):
    p[x] = x
    rank[x] = 0

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py

        if rank[px] == rank[py]:
            rank[py] += 1


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    p = [0] * (n+1)
    rank = [0] * (n+1)

    for i in range(n+1):
        make_set(i)

    for i in range(m):
        st, ed = map(int, input().split())
        union(st, ed)

    ans = 0
    for i in range(1, n+1):
        if i == p[i]:
            ans += 1

    print('#{} {}'.format(tc, ans))