

for tc in range(1, int(input())+1):
    N = int(input())

    check = [0] * 10  # 숫자 췤 빈 리스트
    time = 0  # 곱할 횟수

    while True:

        if 0 not in check:
            break  # 빈 숫자가 없다면 브레이킄


        time += 1   # 곱할 횟수를 하나씩 늘려줌
        num = N * time

        for i in str(num):  # 췤췤
            check[int(i)] = 1

    print('#{} {}'.format(tc, num))

