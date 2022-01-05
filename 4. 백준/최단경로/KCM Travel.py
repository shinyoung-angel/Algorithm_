
import sys
input = sys.stdin.readline



for _ in range(int(input())):
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    cost_table = [[123456789]*(m+1) for _ in range(n+1)]        ## 모든 돈에 대한 거리를 담는 리스트

    for i in range(k):
        st, ed, c, d = map(int, input().split())
        adj[st].append((ed, c, d))


    ## 출발지에 대한 초기화// 1번 노드의 비용은 0이라서
    cost_table[1][0] = 0


    ## m에 대해서 밑으로 쭉 증가하는 방향
    for money in range(m+1):
        for node in range(1, n+1):
            now = cost_table[node][money]
            if now != 123456789:
                for ed, c, d in adj[node]:
                    if money + c <= m:
                        cost_table[ed][money+c] = min(cost_table[ed][money+c], now+d)

    result = min(cost_table[n])

    if result == 123456789:
        print('Poor KCM')
    else:
        print(result)

