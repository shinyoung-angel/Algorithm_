

for tc in range(1, int(input())+1):
    n = int(input())
    num = [0] + list(map(int, input().split()))

    for i in range(2, n+1):

        while True:
            if i < 2:
                break
            if num[i//2] > num[i]:
                num[i//2], num[i] = num[i], num[i//2]
            i //= 2


    ans = 0
    while n >= 1:
        ans += num[n//2]
        n //= 2

    print('#{} {}'.format(tc, ans))



# --------------------------

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    heap = []
    # 최소heap 만들기
    for num in nums:
        heap.append(num)
        idx = len(heap)-1
        # 부모 노드와 비교해서 부모 노드가 자식 노드보다 크면 swap
        while idx > 1 and heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            # swap했다면 루트 노드까지 계속 비교
            idx //= 2
    # 노드 합 구하기
    answer = 0
    while N > 0:
        N //= 2
        answer += heap[N]
    print('#{} {}'.format(tc, answer))


# -------------------------

#################################################

import heapq

for tc in range(1, int(input())+1):
    n = int(input())
    num = [0] + list(map(int, input().split()))

    heap = []

    for i in range(1, n+1):
        heapq.heappush(heap, num[i])

    heap = [0] + heap
    ans = 0
    while n > 0:

        ans += heap[n//2]
        n //= 2

    print('#{} {}'.format(tc, ans))