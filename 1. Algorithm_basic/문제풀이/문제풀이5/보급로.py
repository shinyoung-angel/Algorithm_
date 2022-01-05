from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

##### 주의!!!!!!!!!!!!!! 종료 조건을 함수 안에다 주면 마지막 아이에 대해 상하좌우 돌지 못함 !!!!!!!!!!!!!!

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < n and 0<= nc < n:
                if visited[nr][nc] > visited[r][c] + arr[nr][nc]:
                    visited[nr][nc] = visited[r][c] + arr[nr][nc]
                    queue.append((nr, nc))

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[123456789]*n for _ in range(n)]

    bfs()
    ans = visited[n-1][n-1]

    print('#{} {}'.format(tc, ans))

