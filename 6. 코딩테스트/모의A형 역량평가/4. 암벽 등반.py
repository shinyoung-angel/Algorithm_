# 1
# 5 3
# 300 410 150 55 370
# 120 185 440 190 450
# 165 70 95 420 50


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs():
    pass

for tc in range(int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0]*m for _ in range(n)]
    level = 0

    for i in range(n):
        for j in range(m):




    print('#{} {}'.format(tc, level))

