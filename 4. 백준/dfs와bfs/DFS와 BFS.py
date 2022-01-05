
### 인접리스트로 풀 경우 시작노드가 어느 간선과도 연결되지 않았을 경우를 고려할 수 x

# def dfs(start):
#
#     visited_dfs[start] = 1
#     print(start, end= ' ')
#     for i in adj[start]:
#         if not visited_dfs[i]:
#             dfs(i)
#
# def bfs(start):
#
#     queue = [start]
#     visited_bfs[start] = 1
#     while queue:
#
#         t = queue.pop(0)
#         print(t, end=' ')
#         for i in adj[t]:
#             if not visited_bfs[i]:
#                 queue.append(i)
#                 visited_bfs[i] = 1
#
#
#
# n, m, v = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited_dfs = [0] * (n+1)
# visited_bfs = [0] * (n+1)
#
# for i in range(m):
#     st, ed = map(int, input().split())
#     adj[st].append(ed)
#     adj[ed].append(st)
#
# dfs(v)
# print()
# bfs(v)


# ---------------------

#그래서 인접행렬로 다시 풀었음

def dfs(start):

    visited_dfs[start] = 1
    print(start, end= ' ')
    for i in range(1, n+1):
        if adj[start][i] and not visited_dfs[i]:
            dfs(i)

def bfs(start):

    queue = [start]
    visited_bfs[start] = 1
    while queue:

        t = queue.pop(0)
        print(t, end=' ')
        for i in range(1, n+1):
            if adj[t][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = 1



n, m, v = map(int, input().split())
adj = [[0]*(n+1) for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for i in range(m):
    st, ed = map(int, input().split())
    adj[st][ed] = 1
    adj[ed][st] = 1

dfs(v)
print()
bfs(v)

