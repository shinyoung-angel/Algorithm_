

## m은 현재 계산하는 달
# cost: 이전 달까지의 계산 결과, m은 현재 내가 보낼 결과
def calc(cost, m):
    global min_cost

    # 재귀 멈추는 base case
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return

    # 1일권, 1달권, 3달권 호출할겨
    calc(cost + d*month[m], m+1)
    calc(cost + m1, m+1)
    calc(cost + m3, m+3)

for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    min_cost = y # 1년치 비용이 현재 최저의 가격이라고 가정


    calc(0, 1)
    print('#{} {}'.format(tc, min_cost))


###########################################################



##  dp로 풀기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


for tc in range(1, int(input())+1):
    day, month1, month3, year = map(int, input().split())
    months = [0] + list(map(int, input().split()))

    ## dp에다가 달 별로 최솟값들을 더해줄 것.
    dp = [0] * 13
    dp[1] = min(months[1] * day, month1)

    # 2월부터 12월까지는 이전 달의 비용 더하기 이번 달의 비용
    ## 3개월 이용권은 3개월 전의 가격에다가 더해줄 것임!!!
    #### 1일권, 1개월, 3개월 권의 가격 중 가장 저렴한 아이를 dp에 넣음
    ## 마지막에 year가격과 비교할 것임

    for i in range(2, 13):
        dp[i] = min(dp[i-1]+months[i]*day, dp[i-1]+month1, dp[i-3]+month3)

    print('#{} {}'.format(tc, min(dp[12], year)))