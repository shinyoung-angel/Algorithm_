


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c, color):
    # Q 선언과 동시에 담아놓고 방문쳌
    Q = [(r, c)]
    visited[r][c] = color
    cnt = 0

    while Q:
        curr_r, curr_c = Q.pop(0)
        cnt += 1  # 방문했으니 카운트 하나세기
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            #맵의 범위를 벗어나면 컷
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            #갈수 있다며어어넌
            if arr[nr][nc] == '1' and visited[nr][nc] == 0:
                Q.append((nr,nc))
                visited[nr][nc] = color
    return cnt

def DFS(r,c):
    global home_cnt
    home_cnt += 1
    visited[r][c] = color

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if arr[nr][nc] == '1' and visited[nr][nc] == 0:
            DFS(nr,nc)


N = int(input())  # 단지 N * N

# 붙어져서 들어오는 입력을 받아보자....
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]  # 번호도 넣을거야

ans = []

color = 1

# 아파트 단지를 전체 순회를 하면서 넘버링 해야함.
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == 0:
            #DFS
            home_cnt = 0
            DFS(i,j)
            ans.append(home_cnt)
            #BFS
            # tmp = BFS(i, j, color)
            # ans.append(tmp)

            color += 1

            #확인
            for a in visited:
                print(*a)
            print("-----------------------")

ans.sort()

print(len(ans))
for i in ans:
    print(i)
