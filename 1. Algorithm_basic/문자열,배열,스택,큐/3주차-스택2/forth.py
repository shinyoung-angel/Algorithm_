
# -------------------

for tc in range(1, int(input()) + 1):
    num = list(input().split())

    stack = []
    ans = 1

    for i in range(len(num) - 1):
        if num[i].isdigit():
            stack.append(num[i])

        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())

                if num[i] == '+':
                    stack.append(a + b)
                elif num[i] == '-':
                    stack.append(a - b)
                elif num[i] == '*':
                    stack.append(a * b)
                elif num[i] == '/':
                    stack.append(a // b)
            except:
                ans = False

    if ans == False or len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')
