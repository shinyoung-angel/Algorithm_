

import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

ans = abs(n-100)

for i in range(1000001):
    for j in str(i):
        if int(j) in arr:
            break
    else:
        ans = min(ans, len(str(i)) + abs(n-i))

print(ans)


################

N = int(input())
M = int(input())
L = [1]*10

if M:
    for i in list(map(int ,input().split())):
        L[i] = 0

def clickable(value):
    if value == 0:
        return L[value]

    while value:
        if not L[value % 10]:
            return False
        value //= 10
    return True

if N == 100:
    print(0)
else:
    lower_value,lower_count = 100,0
    upper_value,upper_count = 1000000,0

    for i in range(N,-1,-1):
        if clickable(i):
            lower_value = i
            lower_count = len(str(lower_value))
            break

    if sum(L) != 0:
        i = N
        for i in range(N,1000001):
            if clickable(i):
                upper_value = i
                upper_count = len(str(upper_value))
                break
            i += 1

    # print(lower_value,lower_count,upper_value,upper_count)
    print(min(abs(N-100),abs(N - lower_value) + lower_count, abs(upper_value - N) + upper_count))