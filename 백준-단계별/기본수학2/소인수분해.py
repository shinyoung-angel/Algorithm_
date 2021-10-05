


n = int(input())
ans = []
i = 2

while i <= n:

    if n == 1:
        break

    if n % i == 0:
        ans += [i]
        n //= i
        continue

    i += 1

if ans == 0:
    print()
else:
    for i in ans:
        print(i)
# ----------------------------------------------

a = int(input())
temp = 0
while True:
    for i in range(2,a+1):
        if a % i == 0:
            a = a // i
            temp = -1
            print(i)
            break
    if temp == 0:
        break
    temp = 0

