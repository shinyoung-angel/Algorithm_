
for t in range(1, int(input() ) +1):
    N = int(input())
    TC = list(map(int, input().split()))

    for i in range(len(TC ) -1):
        min_idx = i
        for j in range( i +1, len(TC)):
            if TC[min_idx] > TC[j]:
                min_idx = j

        TC[i], TC[min_idx] = TC[min_idx], TC[i]


    print('#{} {}'.format(t, " ".join(map(str, TC))))

---------------------------------
---------------------------
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    sort_nums = [0] * N

    K = -1
    for i in nums:
        if K < i:
            K = i

    counts = [0] * (K + 1)

    # 카운팅 하기
    for i in range(len(nums)):
        counts[nums[i]] += 1

    # 누적합 counts 리스트
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # 뒤에서 부터 nums를 읽어오면서 자리에 맞게끔 쇽쇽쓱싹쇽
    for i in range(len(nums) - 1, -1, -1):
        # 위치를 찾아보자.
        n = nums[i]
        counts[n] -= 1
        idx = counts[n]
        sort_nums[idx] = n

        # 교재버전
        # sort_nums[counts[nums[i]]-1] = nums[i]
        # counts[nums[i]] -= 1

    print("#{} {}".format(tc, " ".join(map(str, sort_nums))))