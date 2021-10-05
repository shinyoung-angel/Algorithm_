
# 완존탐색
def check():
    global checking, now_check

    # 교환 횟수만큼
    for _ in range(cnt):
        # now_check에 있는 요소들을 하나하나 pop해서 순열을 만들것
        while now_check:
            # now_check에 있는 요소들을 꺼내서 리스트 형태로 만듦
            t = list(now_check.pop())

            ## 모든 경우의 수의 순열을 만들어서 checking 세트에 넣어줌.
            for i in range(numbers_length-1):
                for j in range(i+1, numbers_length):
                    t[i], t[j] = t[j], t[i]
                    checking.add(''.join(t))
                    # 세트에 넣어주고 다시 원래대로
                    t[i], t[j] = t[j], t[i]

        ## while문이 끝나면 checking에 있던 요소들을 검사해줘야하기 때문에
        ## checking에 있던 아이들을 now_check으로 복사해와서 다시 검사 진행
        now_check = checking
        # checking은 다음 교환 횟수를 검사해야하니 비워 줌.
        checking = set()

    # 교환횟수만큼의 검사가 끝났다면 마지막에 남아있는 now_check요소들을 int형으로 바꿔줌
    now_check = map(int, now_check)
    # 그 중 최대값이 증답이다~~!
    return max(now_check)


for tc in range(1, int(input())+1):
    # 숫자판의 정보, 교환 횟수
    numbers, cnt = input().split()
    # 숫자판 숫자 갯수
    numbers_length = len(numbers)
    # 교환 횟수를 int형을 바꿈
    cnt = int(cnt)
    # 숫자판에 있는 숫자들을 하나하나 완전탐색할 것
    now_check = set([numbers])
    ## 징검다리용 set
    checking = set()


    print('#{} {}'.format(tc, check()))

# ---------------------------------
# cnt: 바꾼 횟수
def change(cnt):
    global ans
    curr = int(''.join(money))
    #####################s
    if [curr, cnt] in visited:
        return
    visited.append([curr, cnt])
    #####################

    if cnt == k:
        ans = max(ans, curr)
        return

    for i in range(len(money)-1):
        for j in range(i+1, len(money)):
            money[i], money[j] = money[j], money[i]
            change(cnt+1)
            money[i], money[j] = money[j], money[i]



for tc in range(1, int(input())+1):
    money, k = input().split()
    money = list(money)

    ## 가지치기용 리스트 만둘깅
    visited = []
    k = int(k)

    ans = 0
    check(k)

    print('#{} {}'.format(tc, ans))