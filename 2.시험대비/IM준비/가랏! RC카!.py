

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    velocity = 0

    for i in range(N):

        if arr[i][0] == 1:
            velocity += arr[i][1]
            ans += velocity
        elif arr[i][0] == 2:
            if velocity < arr[i][1]:
                velocity = 0
            else:
                velocity = velocity - arr[i][1]
                ans += velocity
        else:
            ans += velocity

    print('#{} {}'.format(tc, ans))