from collections import deque
import sys
input = sys.stdin.readline

def right(num, dir):

    if num > 4 or gears[num-1][2] == gears[num][6]: return
    if gears[num-1][2] != gears[num][6]:
        right(num+1, -dir)
        gears[num].rotate(dir)

def left(num, dir):

    if num < 1 or gears[num][2] == gears[num+1][6]: return

    if gears[num+1][6] != gears[num][2]:
        left(num-1, -dir)
        gears[num].rotate(dir)

gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, input().strip())))

k = int(input())

for _ in range(k):
    a, b = map(int, input().split())

    right(a+1, -b)
    left(a-1, -b)

    gears[a].rotate(b)


cnt = 0
for i in range(4):
    cnt += gears[i+1][0] * (2**i)

print(cnt)

