import sys
input = sys.stdin.readline
import heapq

n = int(input())

num = [int(input()) for _ in range(n)]
heap = []
for i in range(n):
    tmp = num[i]
    if tmp >= 1: heapq.heappush(heap, tmp)
    else:
        if heap:
            min_value = heap[0]
            print(min_value)
            heapq.heappop(heap)
        else:
            print(0)



