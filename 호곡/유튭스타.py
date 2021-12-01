

# 5 100
#
# 20 500
# 10 1000
# 60 2000
# 80 3000
# 30 1700

n, m = map(int, input().split())
arr = [[0,0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

knapsack = [[0]*(m+1) for _ in range(n+1)]
result = 0

for num in range(1, n+1):
    arr[num][0] /= 2

    for i in range(1, n+1):
        for j in range(1, m+1):
            minute = arr[i][0]
            subscribers = arr[i][1]

            if j < minute:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(subscribers + knapsack[i-1][j-round(minute)], knapsack[i-1][j])

    arr[num][0] *= 2
    result = max(result, knapsack[n][m])

print(result)
