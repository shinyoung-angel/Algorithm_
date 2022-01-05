


for tc in range(1, int(input())+1):
    str = list(input())
    ## 문자열을 딕셔너리로 만들기
    str_dic = {i:0 for i in str}

    ## 문자열의 갯수를 카운트
    for i in str:
        str_dic[i] += 1

    result = []
    ## 갯수가 홀수인 것만 result에 담기
    for item, value in str_dic.items():
        if value % 2 == 1:
            result.append(item)
    ## 정렬
    result.sort()

    if not result:
        result = 'Good'
    else:
        result = ''.join(result)

    print('#{} {}'.format(tc, result))
