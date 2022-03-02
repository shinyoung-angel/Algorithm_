


## heapq를 사용하면 모두 정렬이 잘 될 줄 알았다!
## 하지만 최소힙 기준으로 정렬되는 것이기 때문에 제일 뒤의 값이 최대값이라는 보장이 없다!
## 그래서 땡!!!!
## 결론: 최소힙, 최대힙 두 개의 힙을 생성해야 함!
import heapq
import sys
input = sys.stdin.readline


## 동기화 시켜주는 함수!
## 최소힙에서 삭제된 원소가 있다면 최대힙에서도 삭제해야 함. 그 반대도 마찬가지
def sync(heap):
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)


for tc in range(int(input())):
    n = int(input())
    min_heap = []
    max_heap = []
    ## 방문췤
    visited = [0] * 10000000

    arr = [list(input().split()) for _ in range(n)]

    for i in range(n):
        operation, num = arr[i]

        if operation == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))        ##최대힙
            visited[i] = 1                                  ##안에 숫자가 들어있다, 아직 삭제되지 않음
        else:
            if num == '1':
                sync(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0             ## 최대힙의 최대값 삭제 표시
                    heapq.heappop(max_heap)                 ## 삭제하기
            else:
                sync(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    ## 마무리 동기화 작업
    sync(min_heap)
    sync(max_heap)

    if not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])