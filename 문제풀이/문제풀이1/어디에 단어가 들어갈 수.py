

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0


    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1: # 흰색 부분이양
                cnt_r += 1
            else:
                if cnt_r == K:   #벽이라면
                    ans += 1
                cnt_r = 0

        #끝까지 가서ㅑㅇ 완성된 경우
        if cnt_r == K:
            ans += 1


        # 열 검사

        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

        if cnt_c == K:
            ans += 1

    print('#{} {}'.format(tc, ans))



#___________________ 띠를 두르자


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt_r = 0
        for j in range(N+1):
            if puzzle[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

    print('#{} {}'.format(tc, ans))






