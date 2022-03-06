
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
result = ''

## 재귀 - 색종이 만들기, 조이의 개수 문제와 거의 흡사함
## 차이점은 분할 정복을 시작할 때 (를 붙여주고
## 재귀를 빠져나올 때 )를 붙여줘야 한다는 것
def quad_tree(x, y, num):
    global result

    tmp = arr[x][y]
    for i in range(x, x+num):
        for j in range(y, y+num):
            if arr[i][j] != tmp:
                result += '('
                for k in range(2):
                    for h in range(2):
                        quad_tree(x+k*num//2, y+h*num//2, num//2)
                result += ')'
                return

    if tmp == 0:
        result += '0'
    else:
        result += '1'

quad_tree(0, 0, n)

print(result)




