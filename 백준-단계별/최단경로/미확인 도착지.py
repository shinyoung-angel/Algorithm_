


for tc in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj = [[0]*(n+1) for _ in range(n+1)]

    for i in range(m):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w
        adj[ed][st] = w

    destination = []
    for i in range(t):
        destination.append(int(input()))

