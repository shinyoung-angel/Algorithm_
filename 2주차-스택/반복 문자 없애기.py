
for tc in range(1, int(input()) + 1):
    TC = input()
    stack = []

    for i in TC:
        if len(stack) >= 1 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)


    print('#{}'.format(tc), len(stack))

# --------------------


for _ in range(int(input())):
    L = list(input())
    while 1:
        for i in range(1,len(L)):
            if L[i-1]==L[i]:
                L.pop(i-1)
                L.pop(i-1)
                break
        else:
            break
    print(f'#{_+1} {len(L)}')

