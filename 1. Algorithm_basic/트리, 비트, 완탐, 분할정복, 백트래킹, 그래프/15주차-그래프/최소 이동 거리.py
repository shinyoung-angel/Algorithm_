

for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    arr = [[123456789]*(n+1) for _ in range(n+1)]
    for i in range(e):
        st, ed, w = map(int, input().split())
        arr[st][ed] = w
        # arr[ed][st] = w     ------------> 이거는 무방향이라 땡이야!!!

    key = [123456789] * (n+1)
    visited = [0] * (n+1)
    key[0] = 0

    for _ in range(n):

        min_idx = 0
        min_value = 123456789

        ### 최소 정점의 인덱스 찾기
        for i in range(n+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1

        ## 값 갱신
        for i in range(n+1):
            if not visited[i] and key[i] > key[min_idx] + arr[min_idx][i]:
                key[i] = key[min_idx] + arr[min_idx][i]


    print('#{} {}'.format(tc, key[n]))



#############

def dijkstra():
    key = [123456789] * (v+1)
    visited = [0] * (v+1)
    key[0] = 0

    for _ in range(v):
        min_idx = -1
        min_value = 123456789

        for i in range(1, v+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1

        for i in range(1, n+1):
            if not visited[i] and key[i] > key[min_idx] + arr[min_idx][i]:
                key[i] = key[min_idx] + arr[min_idx][i]

    return key[v]

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    arr = [[123456789]*(v+1) for _ in range(v+1)]

    for i in range(e):
        s, e, w = map(int, input().split())
        arr[s][e] = w                           ## 유향그래프


    print('#{} {}'.format(tc, dijkstra()))