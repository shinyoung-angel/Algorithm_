import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def divide(x, y, cnt):
    global  white, blue

    tmp = arr[x][y]
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            if tmp != arr[i][j]:
                for k in range(2):
                    for h in range(2):
                        divide(x+k*cnt//2,y+h*cnt//2, cnt//2)
                return


    if tmp == 0: white += 1
    else: blue += 1


divide(0,0,n)

print(white)
print(blue)

