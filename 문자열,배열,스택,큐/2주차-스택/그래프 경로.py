

def dfs(start, last):

    stack = []
    visited = [0] * (V+1)
    stack.append(start)

    while stack:

        curr = stack.pop()

        if not visited[curr]:
            visited[curr] = True

            for i in range(1, V+1):
                if not visited[i] and arr[curr][i]:
                    stack.append(i)

    if visited[last] == True:
        return 1
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = 1

    S, G = map(int, input().split())


    print('#{} {}'.format(tc, dfs(S, G)))
