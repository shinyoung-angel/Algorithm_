import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for tc in range(1, int(input())+1):
    n = int(input())
    heap = []
    caught = []
    arr = []
    ans = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] != 0:
                heapq.heappush(heap, [i+j, i, j, tmp[j]])

    while heap:

        for i in range(len(heap)):
            tmp = heap[i]
            if (tmp[3] >= 1) or (tmp[3] < 0 and abs(tmp[3]) in caught):
                now_catch = tmp
                heap.remove(tmp)
                caught.append(tmp[3])
                ans += tmp[0]
                break

        x = now_catch[1]
        y = now_catch[2]

        for i in range(len(heap)):
            heap[i][1] = abs(heap[i][1] - x)
            heap[i][2] = abs(heap[i][2] - y)
            heap[i][0] = heap[i][1] + heap[i][2]



    print('#{} {}'.format(tc, ans))



