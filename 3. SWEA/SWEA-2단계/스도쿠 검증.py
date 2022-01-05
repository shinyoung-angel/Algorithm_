

def check(arr):

    # 가로, 세로 한방에 처리
    # 숫자를 카운트 해서 0인 것이 2개 이상이면 땡!
    for i in range(9):
        counting_r = [0] * 10
        counting_c = [0] * 10

        for j in range(9):
            counting_r[arr[i][j]] += 1
            counting_c[arr[j][i]] += 1
        if counting_r.count(0) >= 2 or counting_c.count(0) >= 2:
            return 0

    # 가로세로 네모네모
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            counting = [0] * 10
            for r in range(i, i+3):
                for c in range(j, j+3):
                    counting[arr[r][c]] += 1
            if counting.count(0) >= 2:
                return 0
    return 1

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, check(arr)))