import sys
input = sys.stdin.readline

arr = []
for i in range(100000):
    tmp = input()
    if tmp == '.': break
    arr.append(tmp)


for i in arr:
    result = 'yes'
    tmp = list(i)
    stack = []

    for j in tmp:
        if j == '(' or j == '[':
            stack.append(j)
        elif stack:
            if j == ')' and stack[-1] == '(':
                stack.pop()
            elif j == ']' and stack[-1] == '[':
                stack.pop()

        elif not stack:
            if j == ']' or j == '(':
                result = 'no'
                break

    if stack:
        result = 'no'

    print(result)


