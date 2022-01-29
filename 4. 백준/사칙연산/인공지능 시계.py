

a, b, c = map(int, input().split())
time = int(input())

while time > 0:

    c += time % 60


    if c >= 60:
        c -= 60
        b += 1
    time -= time % 60

    b += time // 60


    if b >= 60:
        a += b // 60
        b -= b// 60 * 60


    time -= 60 * (time // 60)

a %= 24
print(a, b, c)
