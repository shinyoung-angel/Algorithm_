import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0] * (n+1)
sel = []


def perm(cnt):

    if cnt == m:
        print(*sel)
        return

    for i in range(1, n+1):
        sel.append(i)
        perm(cnt+1)
        sel.pop()

perm(0)