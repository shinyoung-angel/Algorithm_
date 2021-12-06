
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.pop(0)
        old = arr[x][y]
        direction = arr[x][y][1]
        new_x = x + dr[direction]
        new_y = y + dc[direction]
        new = arr[new_x][new_y]

        if 1 <= new_x < n-1 and 1 <= new_y < n-1:
            if new[0] == 0:
                new[0], new[1] = old[0], old[1]
            else:
                new[0] += old[0]
                if new[0] < old[0]:
                    new[1] = old[1]
                    new[2] = old[0]
                else:
                    if old[0] > new[2]:
                        new[1] = old[1]
                        new[2] = old[0]
            old[0], old[1] = 0, 0
        else:
            new[0] = old[0] // 2
            if old[1] == 1 or old[1] == 3:
                new[1] = old[1] + 1
            else:
                new[1] = old[1] - 1
            old[0], old[1] = 0, 0


for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    arr = [[[0,0,0] for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        a, b, micro, d = map(int, input().split())
        arr[a][b] = [micro, d, 0]

    for _ in range(m):
        queue = []
        for i in range(n):
            for j in range(n):
                if arr[i][j][0] >= 1:
                    queue.append((i,j))
        bfs()
    print(arr)
    result = 0
    for i in range(n):
        for j in range(n):
            num = arr[i][j][0]
            if num >= 1:
                result += num

    print('#{} {}'.format(tc, result))

