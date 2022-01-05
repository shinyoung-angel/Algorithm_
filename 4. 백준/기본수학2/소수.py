
### 시간이 11196ms!!!!!!!!!!!! #######################################################

m = int(input())
n = int(input())
num = []


for i in range(m, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
        if cnt >= 3:
            break

    if cnt == 2:
        num += [i]



total = 0
for i in num:
    total += i

if len(num) == 0:
    print(-1)
else:
    print(total, num[0])



# -------------------------

import math
M = int(input())
N = int(input())

arr = []
for i in range(M,N+1):
    check = 0
    num = int(math.sqrt(i))
    if i == 1:
        continue

    for j in range(2, num + 1):
        if i % j == 0:
            check += 1
            break
    if check == 0:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print("{}\n{}".format(sum(arr), min(arr)))