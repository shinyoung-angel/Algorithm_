import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

### 1780.종이의 개수와 거의 흡사한 문제이다
def divide(x, y, cnt):
    global  white, blue

    ## 첫번째 요소를 tmp에 담아주고
    tmp = arr[x][y]
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            if tmp != arr[i][j]:        ## 첫번째 요소와 값이 다르다면 재귀로 들어감
                for k in range(2):
                    for h in range(2):
                        divide(x+k*cnt//2,y+h*cnt//2, cnt//2)
                return  ##### return 잊지 말기!!!!!!!!!!


    if tmp == 0: white += 1
    else: blue += 1


divide(0,0,n)

print(white)
print(blue)

