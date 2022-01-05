import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sel = []

def perm(cnt, idx):

    if cnt == m:
        print(*sel)
        return

    for i in range(idx, n+1):
        sel.append(i)
        perm(cnt+1, i)
        sel.pop()

perm(0, 1)