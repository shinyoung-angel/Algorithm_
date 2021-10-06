

# 1차 리스트를 이용해서 만듦

heap = [0] * 20
heap_size = 0           # 마지막 노드 번호 겸 실제 사용 크기


def heap_push(item):
    global heap_size
    heap_size += 1      # 힙 사이즈를 한 칸 증가시키고
    heap[heap_size] = item      # 해당 자리에 값을 넣는다.

    c = heap_size
    p = heap_size // 2


    # 조건 헷갈리지 않기~~~~~
    while p and heap[p] > heap[c]: # 부모가 있고 부모가 자식보다 더 클 때
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


arr = [7, 6, 5, 8, 9]

for i in arr:
    heap_push(i)
print(heap)


# ------------------------------

def heap_pop():
    global heap_size
    tmp = heap[1]           # 루트 노드의 값을 반환
    heap[1] = heap[heap_size]   # 가장 마지막 노드를 루트 노드로
    heap_size -= 1

    p = 1
    c = p * 2               # 왼쪽 자식을 먼저 생각

    while c <= heap_size:   # 완전 이진트리이므로 왼쪽자식을 확인

        # 오른쪽 자식이 있다면, 최소힙인데 오른쪽 자식 값이 더 작음
        if c+1 <= heap_size and heap[c] > heap[c+1]:
            c += 1

        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2       # 부모자식 다시 세팅

        else:
            break


    return tmp


for i in range(len(arr)):
    print(heap_pop())