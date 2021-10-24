import sys
input = sys.stdin.readline


def perm(cnt, now_idx):

    if cnt == m:
        print(*sel)
        return

    for i in range(now_idx, n+1):
        if not visited[i]:
            sel.append(i)
            visited[i] = 1
            perm(cnt+1, i+1)            #### i+1을 호출!!!!!!!
            visited[i] = 0
            sel.pop()

n, m = map(int, input().split())
sel = []
visited = [0] * (n+1)
perm(0, 1)