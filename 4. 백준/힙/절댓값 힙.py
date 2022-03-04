import heapq
import sys
input = sys.stdin.readline

## 힙 안의 튜플에 두번째 요소는 정렬에 영향을 미치지 않는다고 생각했다.
## 고래서 음수, 양수 분기를 해서 풀었는데..!
## 고럴 필요 없이, 튜플의 0번째, 1번째 요소를 기준으로 자동 정렬이 됨.
## 고 성질을 몰라서 살짝 헤맸다
n = int(input())
num_list = [int(input()) for _ in range(n)]
heap = []

for i in range(n):
    num = num_list[i]

    if num == 0:
        if not heap: print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))



