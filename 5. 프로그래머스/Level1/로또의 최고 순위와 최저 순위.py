def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    ### 겹치는 숫자 개수
    num_cnt = 0
    zero_cnt = 0
    for num in lottos:
        if num in win_nums:
            num_cnt += 1
        if num == 0:
            zero_cnt += 1

    ### 최고 순위, 최저 순위일 때 겹치는 공의 개수
    high = zero_cnt + num_cnt
    low = num_cnt

    ## 순위를 체크해주는 함수
    rank_high = rank(high)
    rank_low = rank(low)

    return [rank_high, rank_low]

########################

## 깔끔한 코드 겟

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]