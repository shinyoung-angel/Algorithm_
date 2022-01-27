import sys
input = sys.stdin.readline

#### 0,1,2,3 방향 --> 3,2,1,0으로 휙 돌림
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

#### 규칙을 알아내는 것이 포인트!!!!!!
n = int(input())

arr = [[0]*101 for _ in range(101)]
curves = [list(map(int, input().split())) for _ in range(n)]

for tmp in curves:
    x, y, d, gen = tmp[0], tmp[1], tmp[2], tmp[3]
    arr[x][y] = 1

    move = [d]

    ### 주어진 세대 수만큼 돌 것이다
    for repeat in range(gen):
        tmp = []
        ### 세대 수를 돌 때 항상 대칭에 있는 숫자에 1을 더해줘야 함.
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1) % 4)
        ## 그 숫자들을 move에 담아주기
        move.extend(tmp)

    ### move에 들어있는 방향들 모두를 돌아주고 쳌해주기
    for i in move:
        nx = x + dr[i]
        ny = y + dc[i]
        arr[nx][ny] = 1
        x, y = nx, ny

### 사각형 쳌 되어있는 아이들을 count
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            ans += 1

print(ans)
