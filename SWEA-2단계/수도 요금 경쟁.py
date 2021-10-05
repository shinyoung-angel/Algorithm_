

for tc in range(1, int(input())+1):
    p, q, r, s, w = map(int, input().split())

    ### A회사
    a_price = w * p

    ### B회사
    if w <= r:
        b_price = q
    else:
        b_price = q + s * (w-r)


    if a_price < b_price:
        print('#{} {}'.format(tc, a_price))
    else:
        print('#{} {}'.format(tc, b_price))
