from collections import  deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]

### 트리의 지름이란
### a = 특정 노드에서 가장 멀리 있는 노드
### a 노드에서 가장 멀리 있는 노드까지의 거리
### '트리의 지름'이란 개념을 알아야 풀 수 있는 문제!

## 무방향 그래프라 서로의 정보를 넣어줌.
for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))

## 방문 쳌 없이 key 값의 유무로 확인
def bfs(start):
    q = deque([start])
    key = [-1] * (n+1)
    key[start] = 0

    while q:
        t = q.popleft()

        for dist, node in arr[t]:
            if key[node] == -1:
                key[node] = dist + key[t]
                q.append(node)

    return key

first = bfs(1)
first_node = first.index(max(first))  ## 1번 노드에서 방문한 거리 중 가장 멀리 있는 노드의 index
ans = max(bfs(first_node))            ## 그 인덱스로부터 다시 가장 멀리있는 노드 찾기
print(ans)

