
ans = []
for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    ## 높이 차이
    diff = b - a
    ## b의 높이는
    height = diff * (diff+1) // 2
    result = height - b
    ans.append('#{} {}'.format(tc, result))

for i in ans:
    print(i)
