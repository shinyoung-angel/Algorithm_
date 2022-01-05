


for tc in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())

    minute = m1 + m2
    hour = h1 + h2

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour >= 13:
        hour -= 12

    print('#{} {} {}'.format(tc,  hour, minute))

