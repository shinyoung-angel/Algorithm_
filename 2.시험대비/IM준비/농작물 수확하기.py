
# 마름모 만드는 로직을 생각하는 것이 관건!

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    mid = N // 2 # 중간지점으로부터 양 옆으로 인덱스를 점점 더했다가 뺄 것임
    start, end = mid, mid
    ans = 0

    for i in range(N):
        for j in range(start, end+1):
            ans += arr[i][j]

        if i < mid:   # 중간보다 위라면 칸을 늘려가고
            start, end = start - 1, end +1
        else: # 중간보다 아래라면 칸을 줄여갈 것임
            start, end = start +1, end - 1

    print('#{} {}'.format(tc, ans))

