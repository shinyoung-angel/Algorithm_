

n = int(input())
time = list(map(int, input().split()))

time.sort()
for i in range(1, n):
    time[i] = time[i] + time[i-1]


print(sum(time))