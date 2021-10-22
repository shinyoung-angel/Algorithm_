
import sys
input = sys.stdin.readline


def bellman(x):
    key[x] = 0
    flag = 0

    for _ in range(n):                              ## 정점의 갯수만큼 반복
        for i in range(1, n+1):                     ## 모든 정점을 방문
            for ed, w in edges[i]:
                if key[i] != 123456789 and key[ed] > key[i] + w:  ## 조건 중요~~!!!!
                    key[ed] = key[i] + w                        ## 현재의 key값이 무한대가 아니고!! 연결 키값이 더 크다면 갱신

                    if _ == n-1:                    ## 원래는 정점-1 만큼 돌지만 정점만큼 반복을 돌려서 혹시 값이 바뀐다면
                        flag = 1                    ## flag 값이 바뀌게 됨. 그 말은 음수 순환이 있다는 뜻 
    return flag

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
key = [123456789] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b,c))

if bellman(1):
    print(-1)
else:
    for i in range(2, n+1):
        print(key[i] if key[i] != 123456789 else -1)



