
for tc in range(1, int(input()) + 1):
    N = int(input())

    pascal = [[1], [1, 1]]
    for i in range(2, N):
        new = [1]
        for j in range(i - 1):
            new += [pascal[i - 1][j] + pascal[i - 1][j + 1]]
        new += [1]
        pascal += [new]

    print("#{}".format(tc))
    for i in range(N):
        print(*pascal[i])
