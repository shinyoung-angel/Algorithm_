

n, m = map(int, input().split())

sel = []
visited = [0]*(n+1)
def comb(cnt):
    if cnt == m:
        print(*sel)
        return
    else:
        for i in range(1, n+1):
            if not visited[i]:
                sel.append(i)
                visited[i] = 1
                comb(cnt+1)
                visited[i] = 0
                sel.pop()
comb(0)