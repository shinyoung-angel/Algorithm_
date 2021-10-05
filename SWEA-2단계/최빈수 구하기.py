



for tc in range(1, int(input())+1):
    n = int(input())
    check = [0] * 101

    num = list(map(int, input().split()))

    for i in num:
        check[i] += 1

#### 최빈수가 여러 개일 때는 index와 find 함수를 사용할 수 없으니 enumerate를 활용하도록!!!

    max_value = max(check)
    idx = [i for i, x in enumerate(check) if x == max_value]

### enumerate의 인덱스 중에 가장 큰 수가 필요하니께
    print('#{} {}'.format(tc, idx[-1]))