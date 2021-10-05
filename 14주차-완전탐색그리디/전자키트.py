


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]


def golfcart(b, a, tmp):
    global ans
    # 다 돌았을 때
    if a == N:
        # 사무실로 돌아올 때의 배터리 추가
        tmp += zido[b][0]
        if tmp <= ans:
            ans = tmp
        return
    for nc in range(1, N):
        # 방문한 적 없는 관리구역이면
        if not visited[nc]:
            visited[nc] = True
            golfcart(nc, a + 1, tmp + zido[b][nc])
            visited[nc] = False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    zido = []
    for _ in range(N):
        zido.append(list(map(int, input().split())))
    visited = [False] * N
    ans = 987654321

    golfcart(0, 1, 0)
    print('#{} {}'.format(t, ans))