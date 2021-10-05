
def check(idx, visited, total):

    if idx >= n:
        if total < min_value:
            min_value = total
        return
    if total > min_value:
        return

    for k in range(n):
        if visited[k] == 0:
            total += arr[idx][k]

            visited[k] = 1

            check(idx+1, visited, total)

            visited[k] = 0
            total -= arr[idx][k]




for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    total = 0
    min_value = 123456

    check(0,visited, total)
    print('#{} {}'.format(tc, min_value))