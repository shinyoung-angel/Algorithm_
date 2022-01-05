
for i in range(1, int(input())+1):
    # 버스 이동 거리/ 종점의 위치/ 충전소 갯수
    K, N, M = map(int, input().split())
    charge = map(int, input().split())
    bus_stop = [0] * (N+1)

    #충전소를 표시하자
    # for k in charge:
    #     bus_stop[k] = 1
    #
    for k in range(M):
        bus_stop[charge[k]] = 1

    bus_idx = 0 #버스의 위치
    ans = 0

    while True:
        #버스가 이동할 수 있는 만큼 가
        bus_idx += K
        if bus_idx >= N:
            break  #종점에 도착하거나 종점을 지나는 경우

        for j in range(bus_idx, bus_idx - K, -1):
            if bus_stop[j]: #값이 있다면
                ans += 1
                bus_idx = j
                break

        else:
            ans = 0
            break

    print('#{} {}'.format(i, ans))

--------------------------------

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = map(int, input().split())
    stop = [0] * (N + 1)

    for i in charge:
        stop[i] = 1

    bus_idx = 0
    ans = 0

    while True:

        bus_idx += K
        if bus_idx >= N:
            break

        for i in range(bus_idx, bus_idx - K, -1):

            if stop[i]:
                ans += 1
                bus_idx = i
                break
        else:
            ans = 0
            break

    print("#{} {}".format(tc, ans))