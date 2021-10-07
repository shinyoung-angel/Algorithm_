
def bfs(start):
    global cnt

    q = [start]
    visited[start] = 1
    while q:

        t = q.pop(0)
        for i in adj[t]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = 1
    return cnt

n = int(input())
edge = int(input())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for i in range(edge):
    st, ed = map(int, input().split())
    adj[st].append(ed)
    adj[ed].append(st)

print(bfs(1))