
N = input()
num = N
cnt = 0

while True:

    if int(N) < 10:

        N = '0' + N

    first = str( int(N[0]) + int(N[1]) )
    second = N[1] + first[-1]
    N = second

    cnt += 1

    if second == num:
        break

print(cnt)

# -------------------



N = int(input())
num = N
cnt = 0

while True:

    if N < 10:

        N = int('0' + str(N))

    first = N // 10
    second = N % 10
    hap = first + second
    N = int(str(second) + str(hap)[-1])

    cnt += 1

    if N == num:
        break

print(cnt)




