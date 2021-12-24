
def Candy(N, M, nums):
    # 가방의 최소개수
    min_num = 1
    # 가방의 최대개수(=사탕 종류 중 가장 많은 사탕의 개수)
    max_num = max(nums)

    # 이분탐색 답을 찾을 때까지
    while min_num <= max_num:
        # 최소 + 최대의 중간 지점 = 가방의 개수라고 가정
        mid_num = (min_num + max_num) // 2
        # 한 가방에 들어가는 사탕의 수
        cnts = 0

        for num in nums:
            # 사탕의 종류별로, 한 가방에 넣을 수 있는 사탕의 수를 cnts에 더해줌
            cnts += num // mid_num

        # 가방에 들어가는 사탕의 수가 문제 조건과 같을 때
        if cnts == M:
            result_nums = []
            for num in nums:
                if num // mid_num != 0: # (사탕 개수 나누기 가방 개수 = 각 가방에 들어가는 사탕의 수)
                    # 의 몫이 0이 아니면, 즉 담을 수 있는 사탕이면,

                    # 사탕의 수를 각 가방에 들어가는 수로 나눈 값을 리스트에 담고
                    result_nums.append(num // (num // mid_num))
            # 가장 적은 값(모든 사탕이 들어갈 수 있는 최대의 가방 개수)을 반환
            return min(result_nums)

            # 사탕 수가 모자라면(가정한 가방 수가 너무 많으면)
        elif cnts < M:
            # 최대 값을 하나 줄여 다시 이분 탐색
            max_num = mid_num - 1
        # 사탕 수가 너무 많으면(가정한 가방 수보다 많이 만들 수 있다면)
        else:
            # 최소 값을 하나 늘려 다시 이분 탐색
            min_num = mid_num + 1

    return max_num


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    nums = [int(i) for i in input().split()]
    result = Candy(N, M, nums)
    print(f'#{t + 1} {result}')