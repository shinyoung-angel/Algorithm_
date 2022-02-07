

n = int(input())

num = 1
total = 0
while total < n:
    total += num
    num += 1


if total > n: print(num-2)
else: print(num-1)

