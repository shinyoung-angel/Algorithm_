import sys
input = sys.stdin.readline

v, e = map(int, input().split())
adj = [[123456789]*(v+1) for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    adj[a][b] = c                       ## 일방 통행 도로

## 자기 자신을 0으로 설정할 필요 xxxxxxxxxx
## 왜냐하면 싸이클을 찾는 문제이기 때문!!!!!
## 싸이클은 자기 자신으로 돌아가는 것을 의미 ex) 1 --> 3-> 2-> 1 이렇게!!!!!!!!
## 따라서 우리가 얻을 값은 adj[i][i]의 값!!!!!!!!!!!

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

### 최소의 사이클을 찾기!!
## 본인에서 본인으로 가는 거리들 중 가장 작은 거리 = 가장 작은 사이클 !!!!!!!!!!!!!!!!!!!!!!!!!!!
result = 123456789
for i in range(1, v+1):
    result = min(result, adj[i][i])

if result == 123456789:
    print(-1)
else:
    print(result)



