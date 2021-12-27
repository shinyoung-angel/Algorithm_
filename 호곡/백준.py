
import sys
input = sys.stdin.readline
from collections import deque

################ visited = [0] * (top+1)로 했을 때는 30%에서 오류가 났다
########근디 0 대신에 -1을 넣으니 통과네,,,,????

top, start, company, u, d = map(int, input().split())
dr = [u, -d]
visited = [0] * (top+1)

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    while queue:
        t = queue.popleft()

        if t == company:
            return
        for i in range(2):
            nt = t + dr[i]
            if 1 <= nt <= top and visited[nt] == 0:
                visited[nt] = visited[t] + 1
                queue.append(nt)

bfs(start)

ans = visited[company]

if ans == 0:
    print('use the stairs')
else:
    print(ans-1)
