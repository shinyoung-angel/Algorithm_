
import sys
input = sys.stdin.readline

def dfs(x):
    global ans

    stack = [x]
    visited[x] = 1

    while stack:
        t = stack.pop()
        ans += 1

        for i in range(1, n+1):
            if not visited[i] and adj[t][i]:
                visited[i] = 1
                stack.append(i)


for tc in range(int(input())):
    n, m = map(int, input().split())
    adj = [[0]*(n+1) for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1

    ans = 0
    dfs(1)


    print(ans-1)