
## 내 제출

def bfs(start):
    cnt = 0
    queue = [start]
    while queue:
        t = queue.pop(0)

        for i in tree[t]:
            queue.append(i)
            cnt += 1

    return cnt


for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    tree = [[] for _ in range(e+2)]

    node = list(map(int, input().split()))
    for i in range(e):
        st = node[i*2]
        ed = node[i*2+1]
        tree[st].append(ed)

    print('#{} {}'.format(tc, bfs(n)+1))



#### 이 코드도 참고하렴


def dfs(idx):
    global count
    # 순회를 할때마다 카운트
    count += 1
    # 자식노드를 순회한다.
    for i in Tree[idx]:
        dfs(i)


for t in range(int(input())):
    # 노드의 개수와 출력할 노드
    E, N = map(int, input().split())
    temp_list = input().split()
    # 노드의 개수만큼 리스트 만들기
    Tree = [[] for _ in range(E + 2)]
    for idx, i in enumerate(range(0, E * 2, 2)):
        a = int(temp_list[i])
        b = int(temp_list[i + 1])
        # 부모노드를 찾아서 자식노드 표현
        Tree[a].append(b)
    count = 0
    dfs(N)
    # 결과값 출력
    print('#{} {}'.format(t + 1, count))


