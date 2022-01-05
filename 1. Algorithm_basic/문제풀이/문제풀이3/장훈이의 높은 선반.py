


for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort()

    height_list = []
    for i in range(1, 1<<n):
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += height[j]
        if total >= b:
            height_list.append(total)

    ans = min(height_list) - b

    print('#{} {}'.format(tc, ans))



## 재귀 가넝~

## powerset(idx,s, rs) # 점원 수, 중간 합, 남은 키의 합
# rs = 전체 점원 키의 합
# idx+1 직원을 뽑
