n = 5
edges = [[0,1],[0,2],[1,3],[1,4]]
def solution(n, edges):
    answer = 2 ** len(edges)
    arr = [[] for _ in range(n)]
    for i in range(len(edges)):
        a, b = edges[i][0], edges[i][1]
        arr[a].append(b)
        arr[b].append(a)

    return answer

print(solution(n, edges))