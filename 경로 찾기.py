

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
node = [[] for _ in range(n)]
for i in range(n):
    tmp = arr[i]
    for j in range(n):
        if tmp[j] == 1:
            node[i].append(j)

result = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def check(start, end):
    pass



for i in range(n):
    for j in range(n):
        if result[i][j] == 0:
            check(i, j)

print(result)
print(visited)





