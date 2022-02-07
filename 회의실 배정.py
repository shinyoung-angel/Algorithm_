

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(reverse=True)
ans = 0

for i in range(len(time)):
    tmp = time[i][0]
    ans += 1
    for j in range(i+1, len(time)):
        remove_list = []
        next_start = time[j][0]
        next_end = time[j][1]
        if next_end > tmp: remove_list.append(j)
    for k in remove_list:
        time.pop(k)

print(ans)


