

# 돈의 종류를 딕셔너리에다가 담고
# 큰 돈부터 해당 액수에서 나눔. 그리고 몫을 해당 액수의 딕셔너리에 추가해줌. 그리고 액수에서 돈만큼 빼줌.


for tc in range(1, int(input())+1):
    n = int(input())

    money = { 50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}


    for i in money:
        a = n // i
        money[i] += a
        n -= a * i
        if n == 0:
            break

    print(f'#{tc}')
    for i in money.values():
        print(i, end=' ')
    print()