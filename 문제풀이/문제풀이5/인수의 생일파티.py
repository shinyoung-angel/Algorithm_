
def dijkstra():
    pass  다익스트라 호출 구현해보아라`````````

for tc in range(1, int(input())+1):
    n ,m ,x = map(int, input().split())
    arr1 = [[123456789]*(n+1) for _ in range(n+1)]      ##원래입력(진출)
    arr2 = [[123456789]*(n+1) for _ in range(n+1)]      ## 뒤집은 입력(진입)

    for i in range(m):
        st, ed, w = map(int, input().split())
        arr1[st][ed] = w
        arr2[ed][st] = w

    key_1 = [123456789] * (n+1)
    key_2 = [123456789] * (n+1)

    ## 다익스트라 호출
    max_value = 0

    for i in range(1, n+1):
        if key_1[i] + key_2[i] > max_value:
            max_value = key_1[i] + key_2[i]

    print('#{} {}'.format(tc, max_value))