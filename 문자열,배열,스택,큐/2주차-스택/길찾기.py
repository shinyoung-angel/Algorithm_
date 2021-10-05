
def dfs():
    stack = []
    visited = [0] * 100
    stack.append(0)

    while stack:

        curr = stack.pop()

        if not visited[curr]:
            visited[curr] = True

            for i in range(100):
                if not visited[i] and arr[curr][i]:
                    stack.append(i)

    if visited[99] == True:
        return 1
    return 0



for tc in range(1, 11):
    TC_num, E = map(int, input().split())

    arr = [[0] * 100 for _ in range(100)]
    position = list(map(int, input().split()))

    for i in range(E):
        start = position[i*2]
        end = position[i*2+1]
        arr[start][end] = 1


    print('#{} {}'.format(tc, dfs()))

####################3

for tc in range(10):
    # t: 테스크케이스 번호, E: 간선의 개수(길의 개수)
    t, E = map(int, input().split())

    edge_list = [[] for _ in range(100)]
    edge_input = list(map(int, input().split()))

    # 화살표 있으면 1로 변경
    for i in range(E):
        start_node = edge_input[i * 2]
        end_node = edge_input[i * 2 + 1]
        edge_list[start_node].append(end_node)

    visited = [False] * 100
    stack = [0]

    while stack:  # stack이 빌 때 까지 반복. 내가 왔던 길을 넣음.
        now = stack.pop()  # 나의 현재위치(현재 있는 노드)

        if not visited[now]:  # 아직 방문 안했으면
            visited[now] = True  # 방문도장 찍어주고

            for v in edge_list[now]:
                if not visited[v]:
                    stack.append(v)

    # 99번에 방문했다면 1 출력, 방문 못했으면(i.e. 값이 1이 아니면) 0 출력
    result = 1 if visited[99] else 0
    print("#{} {}".format(t, result))



for tc in range(10):
    # t: 테스크케이스 번호, E: 간선의 개수(길의 개수)
    t, E = map(int, input().split())

    edge_matrix = [[0 for _ in range(100)] for _ in range(100)]
    edge_input = list(map(int, input().split()))

    # 화살표 있으면 1로 변경
    for i in range(E):
        start_node = edge_input[i * 2]
        end_node = edge_input[i * 2 + 1]
        edge_matrix[start_node][end_node] = 1

    visited = [False] * 100
    stack = [0]

    while stack:  # stack이 빌 때 까지 반복. 내가 왔던 길을 넣음.
        now = stack.pop()  # 나의 현재위치(현재 있는 노드)

        if not visited[now]:  # 아직 방문 안했으면
            visited[now] = True  # 방문도장 찍어주고

            # 모든 노드 반복하면서, 아직 방문 안했으면서 길이 있는 애들은 stack에 넣어줌
            for v in range(100):
                if not visited[v] and edge_matrix[now][v] == 1:
                    stack.append(v)

    # 99번에 방문했다면 1 출력, 방문 못했으면(i.e. 값이 1이 아니면) 0 출력
    result = 1 if visited[99] else 0
    print("#{} {}".format(t, result))