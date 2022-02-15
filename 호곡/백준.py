import sys
input = sys.stdin.readline

tc = int(input())

def bellman(start):

    key = [123456789] * (n+1)
    key[start] = 0

    ## 모든 노드에 대한
    ## 모든 간선을 매번 순회함
    ## 마~~~~~지막 라운드에도 값이 변한다면
    ## 요것은 음수 순환이 있다는 증명
    for i in range(n):
        for a, b, c in edges:
            cost = key[a] + c
            if key[b] > cost:
                key[b] = cost
                if i == n-1:
                    return key

    return key

for i in range(tc):
    n, m, w = map(int, input().split())

    ## 도로는 무방향
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))

    ## 웜홀은 방향
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    print(bellman(1))


