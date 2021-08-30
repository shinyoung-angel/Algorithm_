

for tc in range(1, int(input())+1):
    TC = input()

    stack = []
    ans = 0

    for i in range(len(TC)):
        #열린 괄호면 넣어
        if TC[i] == '(':
            stack.append('(')


        else:
            stack.pop()
            if TC[i-1] == '(':
                ans += len(stack)
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))

# ------------------------------


for tc in range(1, int(input()) + 1):
    TC = input()

    cnt = 0  # 막대기 갯수
    ans = 0

    for i in range(len(TC)):

        if TC[i] == '(':
            cnt += 1

        else:
            cnt -= 1
            if TC[i - 1] == '(':
                ans += cnt
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))



