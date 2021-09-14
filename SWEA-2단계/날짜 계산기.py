

# 만약 5/5 부터 8/15일 까지를 더해야 한다면 5,6,7월 달의 전체 날짜 수를 더하고 5일 + 15일 -1일을 계산해야 함

for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())

    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    ans = 0

    for i in range(m1, m2):
        ans += days[i]

    ans += d2 - d1 + 1

    print('#{} {}'.format(tc, ans))