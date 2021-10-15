
###### 프림

for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    arr = [[123456789]*(n+1) for _ in range(n+1)]

    key = [123456789] * (n+1)
    visited = [0] * (n+1)
    key[0] = 0

    for i in range(e):
        st, ed, w = map(int, input().split())
        arr[st][ed] = w
        arr[ed][st] = w

    ## 최소 인덱스 값 찾기 // 값 갱신
    ## 맨 마지막 정점은 돌지 못함.
    for i in range(n):

        min_idx = -1
        min_value = 123456789

        for i in range(n+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        ### 최소의 정점을 찾고 방문 췤
        visited[min_idx] = 1

        for i in range(n+1):
            if not visited[i] and arr[min_idx][i] < key[i]:
                key[i] = arr[min_idx][i]


    print('#{} {}'.format(tc, sum(key)))




### 크루스칼



def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])          ## 오름차순 정렬

    p = list(range(v + 1))                  ## make_set 과정

    cnt = 0     ## 간선을 선택한 횟수
    ans = 0     ## 가중치를 더한 값
    idx = 0     ## edges 인덱스

    while cnt < v:      # 등호가 필요없음 , 마지막 정점은 오짜피 계산할 수 없으니
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2]
        idx += 1
        
    print('#{} {}'.format(tc, ans))


    ##############################################


def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])  ## 오름차순 정렬

    p = list(range(v + 1))  ## make_set 과정

    cnt = 0  ## 간선을 선택한 횟수
    ans = 0  ## 가중치를 더한 값
    idx = 0  ## edges 인덱스

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):
            cnt += 1
            ans += w
            union(n1, n2)

            if cnt == v:
                break
    print('#{} {}'.format(tc, ans))