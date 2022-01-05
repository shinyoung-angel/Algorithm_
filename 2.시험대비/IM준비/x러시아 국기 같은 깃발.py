


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
























for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    # for row in flag:
    #     print(row)

    # 각 줄에서 화이트 레드 블루 각각의 색으로 바꾸려면 몇번 바꿔야 하는지 2중 배열 형태로 저장한다.
    change_color_cnt = []
    for row in flag:
        w = M - row.count('W')
        b = M - row.count('B')
        r = M - row.count('R')
        change_color_cnt.append([w, b, r])

    answer = 99999999
    # for row in change_color_cnt:
    #     print(row)

    # w와 b 두가지 숫자를 정하면 r은 자동으로 정해진다. w,r은 0부터, b는 최소 1부터이다.
    for w in range(0, N - 3 + 1):
        for b in range(1, N - 2 + 1 - w):
            r = N - w - b - 2

            # 정해진 라인 수 만큼 자신의 색깔로 바꾸는 카운트를 세어준다.
            cnt = 0
            for i in range(w):
                cnt += change_color_cnt[1:-1][i][0]
            for j in range(w, w + b):
                cnt += change_color_cnt[1:-1][j][1]
            for k in range(w + b, w + b + r):
                cnt += change_color_cnt[1:-1][k][2]

            # 최솟값을 찾고
            answer = min(answer, cnt)

    # 맨윗줄과 맨아랫줄도 바꿔준다.
    answer += change_color_cnt[0][0] + change_color_cnt[-1][2]
    print('#{} {}'.format(tc, answer))


T = int(input())
for tc in range(1, T+1):
answer_list = []
N, M = map(int, input().split())
flag = [input() for _ in range(N)]
for i in range(0, N-3+1):
for j in range(i+1, N-2+1):
# (0, i) (i+1, j) (j+1, N-1)
answer = 0
for w in flag[:i+1]:
for x in w:
if x != 'W':
answer += 1
for b in flag[i+1:j+1]:
for y in b:
if y != 'B':
answer += 1
for r in flag[j+1:]:
for z in r:
if z != 'R':
answer += 1
answer_list.append(answer)
print(f'#{tc} {min(answer_list)}')


출처: https://ahyeonlog.tistory.com/13 [기록]