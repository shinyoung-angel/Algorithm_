
## 이중 포문이라 시간초과 발생할 것
for tc in range(1, int(input()) +1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    for i in range(N-1):
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]


        if max_cost > cost[i]:
            ans += max_cost - cost[i]


    print('#{} {}'.format(tc, ans))


#------------------------
# 반대로 생각하기

for tc in range(1, int(input()) + 1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    max_cost = cost[-1]

    for i in range(N-2, -1, -1):
        # 내가 가진 값보다 확인하고 있는 값이 작을 때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]

        else:
            max_cost = cost[i]

    print('#{} {}'.format(tc, ans))







# -----------------------

#-------------------


for tc in range(1, int(input()) + 1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [0] * N

    #사는 게 이득인지 아닌지
    for i in range(N-1):
        for j in range(1+i, N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break

    buy_cost = 0
    buy_cnt = 0

    for i in range(N):
        if is_sell[i]:
            buy_cost += cost[i]
            buy_cnt += 1
        else:
            ans += (cost[i] * buy_cnt) - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print('#{} {}'.format(tc, ans))



