import sys
input = sys.stdin.readline


### 간단한 bfs문제이다.

## 케빈 베이컨의 수를 찾는 함수 check
def check(person):
    queue = [person]
    visited[person] = 0

    while queue:
        t = queue.pop(0)

        for i in range(1, n+1):
            if arr[t][i] and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[t] + 1


n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
result = []

## 아는 사람 연결
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

## n명을 check함
for i in range(1, n+1):
    visited = [-1] * (n + 1)
    check(i)
    result.append(sum(visited[1:]))

## 최소의 값을 가진 인덱스를 찾기!
min_value = min(result)
ans = result.index(min_value) + 1
print(ans)