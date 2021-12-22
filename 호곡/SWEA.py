

n, k = map(int, input().split())

queue = list(range(1, n+1))
tmp = 0
result = []
while queue:

    for i in range(k-1):
        queue.append(queue.pop(0))
    result.append(queue[0])
    queue.pop(0)


result = str(result)
ans = '<'+ result[1:-1] + '>'
print(ans)
