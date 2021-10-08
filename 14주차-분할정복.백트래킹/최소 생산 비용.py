
# idx: 열의 인덱스, cnt: 가능한 경우의 수의 합
def min_cost(idx, cnt):
    global total

    if total <= cnt:            # 가지치기
        return

    if idx == n:                # 가능한 열을 다 돌았음
        total = cnt             # 위에서 가지치기를 했으니 바로 total에 cnt를 할당.

    for i in range(n):
        if not visited_row[i]:  # 방문하지 않은 행이라면
            visited_row[i] = 1  # 방문 췤
            min_cost(idx+1, cnt + cost[i][idx]) # 재귀 호출 /// 해당 행열의 값을 더해줌.
            visited_row[i] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    visited_row = [0] * n       # 행을 갔다 왔는지 췤
    total = 123456
    min_cost(0, 0)

    factory2(0, 0, 0)

    print('#{} {}'.format(tc, total))

# ---------------------------

#### 비트 마스킹

def factory2(idx, cnt, visit):            # 제픔번호//중간게산 결과///정수
    global total

    if total <= cnt:            # 가지치기
        return

    if idx == n:                # 가능한 열을 다 돌았음
        total = cnt             # 위에서 가지치기를 했으니 바로 total에 cnt를 할당.
        return

    for j in range(n):          # 공장을 고르자!!
        if visit & (1<<j): continue
        factory2(idx+1, cnt+cost[idx][j], visit | (1<<j) )


