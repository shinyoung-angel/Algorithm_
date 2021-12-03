


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    people = []
    stair = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                people.append((i,j))
            elif arr[i][j] >= 2:
                stair.append((i, j))

