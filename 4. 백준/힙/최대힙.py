import heapq
import sys
input = sys.stdin.readline

## 최대힙을 구하는 문제이기 때문에
## heap에다가 -를 붙여서 넣으면 최소힙이 최대힙이 된다
n = int(input())
heap = []
for _ in range(n):
    tmp = int(input())

    heapq.heappush(heap, -tmp)

    if tmp == 0: print(-heapq.heappop(heap))

