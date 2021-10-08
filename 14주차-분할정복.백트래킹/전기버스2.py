
def move(idx, e, c):        # 현재 있는 버스정류장 번호// 잔여 배터리// 교환 횟수
    global ans
    if idx == bus_stop[0]:

        if ans > c:
            ans = c

    else:
        ### 교체하지 않고 내려 보내기 ( 배터리가 방전이 되지 않았을 때)
        if e > 0:
            move(idx+1, e-1, c)

        ### 교체하고 내려 보내기

        if c < ans:
            move(idx+1, bus_stop[idx]-1, c+1)

for tc in range(1, int(input())+1):
    bus_stop = list(map(int, input().split()))  #0번 인덱스: 정류장 수//// 나머지는 충전지

    ans = 123456789

    move(2, bus_stop[1]-1, 0)

    print('#{} {}'.format(tc, ans))

