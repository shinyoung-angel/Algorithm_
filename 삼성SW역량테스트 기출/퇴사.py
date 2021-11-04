
import sys
input = sys.stdin.readline



def check(index):

    price = info[index][1]

    time = info[index][0] + index

    if time > n+1:
        return 0
    else:

        while time <= n+1:

            price += info[time][1]

    return price


n = int(input())
info = [[0, 0] for _ in range(n+1)]
result = 0

for i in range(1, n+1):
    t, p = map(int, input().split())
    info[i][0] = t
    info[i][1] = p

for i in range(1, n+1):
    if check(i) > result:
        result = check(i)

print(result)



