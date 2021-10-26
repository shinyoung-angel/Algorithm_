import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
adj = [[123456789]*(n+1) for _ in range(n+1)]


## 이 과정이 없으면 안된다~~~~~~~~~~~~~~
for i in range(m):
    a, b, c = map(int, input().split())
    if adj[a][b] > c:
        adj[a][b] = c

## 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            adj[i][j] = 0


## 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):         ## 거쳐가는 정점
    for a in range(1, n+1):     ## 시작 정점
        for b in range(1, n+1): ## 도착 정점
            adj[a][b] = min(adj[a][b], adj[a][k]+adj[k][b])

## 연결되지 않은 도시들은 0으로 출력하기
for i in range(1, n+1):
    for j in range(1, n+1):
        if adj[i][j] == 123456789:
            print(0, end=' ')
        else:
            print(adj[i][j], end=' ')
    print()