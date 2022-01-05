
### 이분탐색!!


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    min_value = 1
    max_value = max(nums)

    ### 최소, 최대값이 같을 때까지만!
    while min_value <= max_value:
        mid = (min_value + max_value) // 2      ## 가방의 갯수!!!! 가방의 갯수를 이분 탐색을 통해 줄여나가는 것
        cnt = 0                                 ## 가방 하나에 들어가는 사탕의 개수
        for num in nums:                        ## 사탕 개수 // 가방 개수를 다 더하기
            cnt += num // mid

        if cnt < m:                             ## 가방이 너무 많아서 들어갈 사탕이 없다
            max_value = mid - 1                 ## 최대값을 줄이기
        else:                                   ## 가방이 적다
            min_value = mid + 1                 ## 최소값을 늘리기

    print('#{} {}'.format(tc, max_value))