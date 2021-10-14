from collections import deque

def bfs():

    queue = deque([n])
    visited[n] = 1

    while queue:

        t = queue.popleft()

        if t == m:
            return

        for i in [-1, +1, t, -10]:
            nt = t + i

            if 0 <= nt < len(visited) and not visited[nt]:
                visited[nt] = visited[t] + 1
                queue.append(nt)



for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    bfs()

    print('#{} {}'.format(tc, visited[m]-1))