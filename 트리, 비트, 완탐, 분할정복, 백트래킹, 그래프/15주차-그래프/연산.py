from collections import deque

def bfs():

    queue = deque([n])
    visited[n] = 1

    while queue:
        t = queue.popleft()

        if t == m:
            return
        for i in [-1, +1, t, -10]:
            nt = t + i

            if 0 <= nt < len(visited) and not visited[nt]:
                visited[nt] = visited[t] + 1
                queue.append(nt)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    bfs()

    print('#{} {}'.format(tc, visited[m]-1))

##################################################


## 선형 큐 직접 구현

def calc(n, idx):
    if idx == 0: return n +1
    elif idx == 1: return n - 1
    elif idx == 2: return n *2
    else: return  n -10


def bfs():

    queue = [0] * 1000001
    front = rear = -1

    rear += 1
    queue[rear] = n
    visited[n] = 1

    while front != rear :               # 같으면 멈춘다!!

        front += 1
        t = queue[front]

        if t == m:                      ## 지금 뽑은 값이 m과 같다면 해당 횟수를 반환
            return visited[t] -1
        for i in range(4):
            next_num = calc(t, i)

            if 0 <= next_num < 1000001 and visited[next_num] == 0:
                visited[next_num] = visited[t] + 1
                rear += 1
                queue[rear] = next_num

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001

    print('#{} {}'.format(tc, bfs()))




##########################

# 무슨 소린지 잘 모르겠다
from collections import deque

def bfs():

    queue = deque([n])
    visited[n] = 1

    ans = 0

    while queue:
        size = len(queue)

        for i in range(size):
            num = queue.popleft()
            if num == m: return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not visited[j]:
                    visited[j] = 1
                    queue.append(j)

        ans += 1

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001


    print('#{} {}'.format(tc, bfs()))