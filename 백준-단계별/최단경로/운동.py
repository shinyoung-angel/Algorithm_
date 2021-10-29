


v, e = map(int, input().split())
adj = [[123456789]*(v+1) for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    adj[a][b] = c



