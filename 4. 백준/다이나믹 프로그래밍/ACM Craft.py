from collections import deque
import sys
input = sys.stdin.readline

def topology():

    while queue:
        t = queue.popleft()

        for j in tree[t]:
            in_degree[j] -= 1
            dp[j] = max(dp[j], dp[t]+time[j])
            if in_degree[j] == 0:
                queue.append(j)

    return dp

for tc in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    dp = [0] * (n+1)

    ## 정보 담기
    for _ in range(k):
        a, b = map(int, input().split())
        tree[a].append(b)
        in_degree[b] += 1

    destination = int(input())

    ## 시작점 찾기: in_degree 차수가 0인 아이
    queue = deque([])
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    dp_return = topology()

    print(dp_return[destination])



