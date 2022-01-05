import sys

input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False]*N

answer = 0
while True:
    answer += 1
    belt.insert(0, belt.pop())
    robot.insert(0, robot.pop())
    robot[N-1] = False

    for i in range(N-2, -1, -1):
        if robot[i] and robot[i+1] == False and belt[i+1]:
            belt[i+1] -= 1
            robot[i] = False
            robot[i+1] = True
    robot[N-1] = False

    if belt[0] and robot[0] == False:
        belt[0] -= 1
        robot[0] = True

    count = belt.count(0)
    if count >= K:
        break

print(answer


##############

import sys
from _collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False]*N)

answer = 0
while True:
    answer += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False

    for i in range(N-2, -1, -1):
        if robot[i] and robot[i+1] == False and belt[i+1]:
            belt[i+1] -= 1
            robot[i] = False
            robot[i+1] = True
    robot[N-1] = False

    if belt[0] and robot[0] == False:
        belt[0] -= 1
        robot[0] = True

    count = belt.count(0)
    if count >= K:
        break

print(answer)

