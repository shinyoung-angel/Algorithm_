

n = int(input())
m = int(input())
if m != 0:
    arr = list(map(int, input().split()))
    arr.sort()

result = 123456879

able = []
def check(num):
    global result
    ## 사용 가능한 숫자들을 뽑아놓기
    for i in range(10):
        if i not in arr:
            able.append(i)

    ## 가장 가까운 수를 찾기

result = 0
if n == 100:
    pass
elif m == 0:
    result = min(len(str(n)), n-100)
else:
    check(n)

print(result)
