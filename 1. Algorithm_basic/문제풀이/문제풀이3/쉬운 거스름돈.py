###################dp로도 풀어보기

# while문으로 하면 시간 뱅글뱅글 초과,, 왜??
### 9999원은 오똨[,,,,????

for tc in range(1, int(input())+1):
    money = int(input())

    unit = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    for i in unit:
        if money >= i:
            cnt = money // i
            unit[i] += cnt
            money -= i * cnt
        if money == 0:
            break

    print(f'#{tc}')
    for i in unit.values():
        print(i, end= ' ')
    print()

# ---------------------


###
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(int(input())):
    print(f'#{tc + 1}')
    N = int(input())
    ans = [0] * 8
    for i in range(8):
        while N >= money[i]:
            ans[i] += 1
            N -= money[i]
    print(*ans)