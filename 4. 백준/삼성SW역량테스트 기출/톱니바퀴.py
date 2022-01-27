import sys
input = sys.stdin.readline


def right(num):

    if num == 3: return
    else:
        if num_list[num][2] != num_list[num+1][6]:
            if dir_list[num] == 1:
                dir_list[num+1] = -1
            elif dir_list[num] == -1:
                dir_list[num+1] = 1
        right(num+1)

def left(num):

    if num == 0: return
    else:
        if num_list[num][6] != num_list[num-1][2]:
            if dir_list[num] == 1:
                dir_list[num - 1] = -1
            elif dir_list[num] == -1:
                dir_list[num - 1] = 1
        left(num - 1)


num_list = [list(map(int, input().strip())) for _ in range(4)]
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    dir_list = [0] * 4
    dir_list[a-1] = b
    right(a-1)
    left(a-1)

for i in range(4):
    if dir_list[i] == 1:
        try:
            num_list[i].index(0, num_list[i].pop())
        except:
            pass
    elif dir_list[i] == -1:
        num_list[i].append(num_list[i].pop(0))

cnt = 0
for i in range(4):
    cnt += num_list[i][0] * (2**i)

print(cnt)


#########################################################

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



