

n = int(input())

for i in range(n):
    object_sum = i
    num = str(i)

    for j in num:
        object_sum += int(j)

    if n == object_sum:
        print(int(num))
        break

else:
    print(0)
