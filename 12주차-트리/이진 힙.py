

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



# --------------------------------


# 12513. 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

def node_node(_i, _num):
    if _i == 1:
        return

    if nodes[_i // 2] > _num:
        nodes[_i] = nodes[_i // 2]
        nodes[_i // 2] = _num
        node_node(_i // 2, nodes[_i // 2])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nodes = [0] * (N + 1)
    i = 1
    for num in nums:
        nodes[i] = num
        node_node(i, num)
        i += 1

    result = 0
    while N > 1:
        N //= 2
        result += nodes[N]
    print('#{} {}'.format(tc, result))

# --------------------------

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0]
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

def heap_sort(node):
    mom_node = node // 2
    if mom_node < 0:
        return
    else:
        if tree[mom_node] > tree[node]:
            tree[node], tree[mom_node] = tree[mom_node], tree[node]
            heap_sort(mom_node)


for test in range(1, int(input()) + 1):
    N = int(input())
    tree = [0]
    node_num = 1
    for num in map(int, input().split()):
        tree.append(num)
        heap_sort(node_num)
        node_num += 1
    sum_value = 0
    while N:
        N //= 2
        sum_value += tree[N]

    print(f'#{test} {sum_value}')