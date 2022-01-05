

for tc in range(1, int(input()) + 1):
    TC = input()
    stack = []
    ans = 1

    for i in TC:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':

            if len(stack) == 0:
                ans = 0
                break

            if stack[-1] == '(':
                stack.pop()

            else:
                ans = 0
                break

        elif i == '}':

            if len(stack) == 0:
                ans = 0
                break

            if stack[-1] == '{':
                stack.pop()

            else:
                ans = 0
                break

    if stack:
        ans = 0

    print('#{} {}'.format(tc, ans))

