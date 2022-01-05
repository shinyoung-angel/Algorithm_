
import sys
input = sys.stdin.readline

def bfs(r, c):
    queue = [(r, c)]
    visited.append([r,c])
    while queue:
        x, y = queue.pop(0)
        ## 페스티벌 좌표에 다다르면 happy를 출력
        if x == store[-1][0] and y == store[-1][1]:
            print('happy')
            return
        ## store에 담겨 있는 좌표 중에 현재의 거리와의 차이가 1000이하라면
        ## queue에 넣고, 방문 쳌을 한다.
        for nx, ny in store:
            dist = abs(x-nx) + abs(y-ny)
            if dist <= 1000 and [nx, ny] not in visited:
                queue.append((nx, ny))
                visited.append([nx, ny])

    print('sad')

for tc in range(int(input())):
    ## 편의점 갯수
    n = int(input())
    house_x, house_y = map(int, input().split())
    store = []
    for _ in range(n+1):
        tmp = list(map(int, input().split()))
        store.append(tmp)

    visited = []
    bfs(house_x, house_y)


#####################

# def case():
#     q = deque([start])
#     visited = set()
#     while q:
#         x, y = q.popleft()
#         if abs(x - dest[0]) + abs(y - dest[1]) <= 1000:
#             return True
#         for i in range(n):
#             if i not in visited:
#                 nx, ny = store[i]
#                 if abs(x - nx) + abs(y - ny) <= 1000:
#                     q.append([nx, ny])
#                     visited.add(i)
#     return False
#
#
# for i in range(t):
#     n = int(sys.stdin.readline())
#
#     start = list(map(int, sys.stdin.readline().split()))
#     store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#     dest = list(map(int, sys.stdin.readline().split()))
#
#     if case():
#         print("happy")
#     else:
#         print("sad")

