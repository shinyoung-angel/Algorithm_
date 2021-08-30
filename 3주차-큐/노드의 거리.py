
def bfs(s, end):

    q = []
    visited = [0] * (V+1)
    q.append(s)
    visited[s] = 1

    while q:

        t = q.pop(0)

        for i in range(1, V+1):
            if arr[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    if visited[end]:
        return visited[end] - 1
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = 1
        arr[ed][st] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S,G)))