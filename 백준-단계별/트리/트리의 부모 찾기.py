

import sys
sys.setrecursionlimit(10**8)

def dfs(start):

    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i)


n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for i in range(n-1):
    st, ed = map(int, sys.stdin.readline().split())
    tree[st].append(ed)
    tree[ed].append(st)

dfs(1)

for i in range(2, n+1):
    print(parent[i])