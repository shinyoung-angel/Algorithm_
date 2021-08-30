
# 회문2
for tc in range(1, 11):  # case 반복
    T = int(input())  # case 수
    N = [list(input()) for _ in range(100)]  # 갯수 와 반복구문의 길이
    cnt = 0  # 회문의 길이
    for i in range(100):  # 가로 찾기
        for j in range(100):  #
            for k in range(99, 0, -1):  # 회문의 길이
                if j + k <= 100:  # 인덱스 100이하
                    for l in range(k // 2):  # 회문찾을 반값
                        if N[i][j + l] != N[i][j + k - 1 - l]:  # 앞뒤가 같지않으면
                            break  # k 증가
                    else:
                        if cnt < k:  # 최대값을 k 로 갱신
                            cnt = k
                            break

    for i in range(100):  # 세로 찾기
        for j in range(100):  #
            for k in range(99, 0, -1):  # 회문의 길이
                if j + k <= 100:
                    for l in range(k // 2):
                        if N[j + l][i] != N[j + k - 1 - l][i]:
                            break
                    else:
                        if cnt < k:
                            cnt = k
                            break

    print("#{} {}".format(tc, cnt))  # case 마다 출력

## 내가 푼거


def maxmax(data, M):
    length = 0

    for i in range(100):

        for j in range(100 - M + 1):
            if data[i][j:j + M] == data[i][j:j + M][::-1]:
                length = len(data[i][j:j + M])
                return length

        for j in range(100 - M + 1):
            new = []
            for k in range(M):
                new.append(data[j + k][i])

            if new == new[::-1]:
                length = len(new)
                return length

    return None


for tc in range(1, 11):
    N = int(input())
    c = [list(input()) for _ in range(100)]

    new = []

    # 빈 리스트 new에다가 길이들을 다 더해준다. i의 범위가 1부터 100이라 제일 긴 숫자가 제일 뒤에 온다.
    for i in range(1, 101):
        ans = maxmax(c, i)
        if ans:
            new.append(ans)

    ans = new[-1]

    print('#{} {}'.format(tc, ans))






#--------너 천재니

for t in range(10):
    tc = int(input())
    words = [list(input()) for _ in range(100)]
    cnt = 1
    for trans in range(2):
        for i in range(99):
            for j in range(99):
                for w in range(100 - j, cnt, -1):
                    if words[i][j:j + w] == words[i][j + w - 1:j - 1:-1]:
                        if w > cnt:
                            cnt = w
                            break

        for x in range(100):
            for y in range(100):
                if x > y:
                    words[x][y], words[y][x] = words[y][x], words[x][y]

    print("#{} {}".format(tc, cnt))
