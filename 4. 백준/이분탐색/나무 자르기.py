## 문제를 계속 풀다보니 이분탐색 문제는 감이 오구먼

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

#### low를 0에서 1로 바꾸니 정답이다!!!!
low = 1
high = max(trees)

while low <= high:
    mid = (low+high) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += (tree - mid)

    ### h가 너무 높을 때, 최대값을 줄여 줌
    if cnt < m :
        high = mid - 1
    else:
        low = mid + 1

print(high)