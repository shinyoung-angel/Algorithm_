## 모든 노드들이 출발점이 되어서 모든 노드를 방문할 것임
## 그 중 가장 오래 돌아다닌 아이가 정답

def dfs(idx, cnt):
    global ans

    if cnt > ans:
        ans = cnt

    visited[idx] = 1

    for i in adj[idx]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = 0


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]


    for i in range(m):
        st, ed = map(int, input().split())
        adj[st].append(ed)
        adj[ed].append(st)

    ans = 0
    for i in range(1, n+1):
        visited = [0] * (n+1)
        dfs(i, 1)

    print('#{} {}'.format(tc, ans))