from collections import deque
import copy,sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
safe_area = 0

## 3. 바이러스 퍼짐 & 안전영역 갯수 쳌

def virus():
    global safe_area

    # queue = virus_location   --> 이렇게 바이러스 위치를 담아두고 사용하면 에러가 난다~~~!!!
    #### 매번 검사를 해줘야하기 때문에 딥카피 필수~~
    n_arr = copy.deepcopy(arr)
    queue = deque()
    ## 바이러스 위치 담아줌
    for i in range(n):
        for j in range(m):
            if n_arr[i][j] == 2:
                queue.append((i,j))
    ## 바이러스 퍼뜨리기
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < n and 0 <= ny < m:
                if n_arr[nx][ny] == 0:
                    n_arr[nx][ny] = 2
                    queue.append((nx, ny))

    # 안전영역 갯수 쳌
    ### 이중 for문으로 쳌하면 시간초과~~~~~
    cnt = 0
    for i in n_arr:
        cnt += i.count(0)
    safe_area = max(cnt, safe_area)

## 1. 바이러스 위치를 담아 줌 ㄴㄴㄴㄴ --> 여기서 오류 발생
# virus_location = []
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 2:
#             virus_location.append((i,j))

## 2. 벽을 선택하고 바이러스를 퍼뜨림
def walls(wall_cnt):
    if wall_cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                walls(wall_cnt+1)
                arr[i][j] = 0
walls(0)


print(safe_area)
