


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = []
    for i in range(N):
        q.append([cheese[i], i])

    i = 0
    while len(q) > 1:
        q[0][0] //= 2

        if q[0][0] == 0:
            if N+i < M:
                q.pop(0)
                q.append([cheese[N+i], N+i])
                i += 1
            elif N+i >= M:
                q.pop(0)

        else:
            q.append(q.pop(0))

    print('#{} {}'.format(tc, q[0][1]+1))


def cook(p):
    idx_c = N
    pizza = p[:N]
    while pizza:
        pizza[0][1] //= 2  # 치즈 녹음
        temp = pizza.pop(0)  # 확인
        if temp[1] == 0:  # 다녹았네?
            if idx_c < M:  # 넣을거 있으면 넣고
                pizza.append(cheese[idx_c])
                idx_c += 1
        else:  # 안녹았으면 그대로 넣고
            pizza.append(temp)
    return temp[0]


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # 화덕 크기와 피자 개수
    cheese = [[idx + 1, v] for idx, v in enumerate(map(int, input().split()))]
    print("#{} {}".format(tc, cook(cheese)))
