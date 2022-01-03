

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
result = []
cnt = 0
check = False
for num in range(1, n+1):
    stack.append(num)
    result.append('+')
    while True:

        if len(stack) >= 2 and arr[cnt] in stack[:-1]:
            check = True
            break
        if stack[-1] == arr[cnt]:
            stack.pop()
            result.append('-')
            cnt += 1
        else:
            continue
    if check == True:
        break

if check == True:
    print('NO')
else:
    for i in result:
        print(i)