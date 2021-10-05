
## 이건 무슨소린지 잘 모르겠다
for tc in range(int(input())):
    x, y = map(int, input().split())
    distance = y-x

    count = 0  # 이동 횟수
    move = 1   ## count별로 이동 가능한 거리
    total = 0  ### 이동한 거리의 합

    while total < distance:
        count += 1
        total += move ## count 수에 해당하는 move를 더함
        if count % 2 == 0: ## count가 2의 배수라면
            move += 1

    print(count)


# ---------------------------

for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    num = int(distance**0.5)

    if distance <= 3:
        print(distance)
    else:
        if distance == num ** 2:  # 거리가 제곱이라면 제곱근*2-1
            print(2*num -1)
        elif num**2 < distance <= num**2 + num:
            print(2*num)
        else:
            print(2*num+1)
