
import sys

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())
    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5

    ## 원이 일치하는 경우 좌표는 무한대
    if distance == 0 and r1 == r2:
        print(-1)
    ## 두 점에서만 만나는 경우
    elif abs(r1-r2) < distance < abs(r1+r2):
        print(2)
    ## 접하는 경우 가능성은 하나
    elif distance == r1+r2 or distance == abs(r1-r2):
        print(1)
    else:
        print(0)

