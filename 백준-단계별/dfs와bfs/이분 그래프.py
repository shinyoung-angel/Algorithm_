import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):

    queue = deque([x])
    visited[x] = 1

    while queue:
        t = queue.popleft()

        for i in arr[t]:
            if visited[i] == 0:                     ## 아직 방문하지 않았다면 큐에 삽입
                queue.append(i)
                visited[i] = visited[t] * (-1)      ## 인접 노드는 -1 을 곱해서 방문 췤 ( 같은 깊이별로 췤)
            elif visited[i] == visited[t]:          ## 이미 방문한 경우 false
                return 0

    return 1

for tc in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        st, ed = map(int, input().split())
        arr[st].append(ed)
        arr[ed].append(st)


    flag = True
    for i in range(1, v+1):
        if not visited[i] and not bfs(i):
            flag = 0
            break

    if flag:
        print('YES')
    else:
        print('NO')

