

for tc in range(int(input())):
    ## 편의점 갯수
    n = int(input())
    house_x, house_y = map(int, input().split())
    store = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        store.append(tmp)
    fest_x, fest_y = map(int, input().split())
    distance = 0
    ## 편의점이 없는 경우
    result = 'happy'
    if n == 0:
        distance = abs(house_x-fest_x) + abs(house_y-fest_y)
        if distance > 1000:
            result = 'sad'
            break
    else:
        for num in range(n):
            store_x = store[num][0]
            store_y = store[num][1]
            if num == 0:
                distance = abs(house_x-store_x) + abs(house_y-store_y)
                now_x = store_x
                now_y = store_y
            else:
                distance = abs(now_x - store_x) + abs(now_y - store_y)
                now_x = store_x
                now_y = store_y

            if distance > 1000:
                result = 'sad'
                break

        distance = abs(fest_x - now_x) + abs(fest_y - now_y)
        if distance > 1000:
            result = 'sad'
            break

    print(result)




