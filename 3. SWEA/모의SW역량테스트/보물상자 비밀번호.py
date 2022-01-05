

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    hexa = list(input())

    ## 회전 횟수
    rotate = (n//4)
    ## 받아오는 아이들은 중복이 없어야 함.
    nums = set()
    ## 해당 횟수만큼 회전을 할 것임
    for i in range(rotate):
        ## 첫번째 회전을 제외하고서는 숫자 리스트가 한 칸씩 미렬야 함.
        if i != 0:
            ## 끝을 pop하고 다시 앞에다 insert 해줌.
            a = hexa.pop()
            hexa.insert(0, a)
        for j in range(4):
            ### 리스트 형태로 받아왔기 때문에 join으로 문자열로 바꿔준 후 nums라는 set에 추가해줌.
            hexa_component = ''.join(hexa[j*rotate:(j+1)*rotate])
            nums.add(hexa_component)
    ## set이기 때문에 다시 list로 변경 후 내림차순 정렬
    nums = list(nums)
    nums.sort(reverse=True)
    ## k번째 수를 골라 10진수로 변환
    print('#{} {}'.format(tc, int(nums[k-1], 16)))








