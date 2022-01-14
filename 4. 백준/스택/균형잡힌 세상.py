# import sys
# input = sys.stdin.readline

arr = []
while True:
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
        elif j == ')':
            if not stack or stack[-1] == '[':
                result = 'no'
                break
            elif stack[-1] == '(':
                stack.pop()

        elif j == ']':
            if not stack or stack[-1] == '(':
                result = 'no'
                break
            elif stack[-1] == '[':
                stack.pop()
    if stack:
        result = 'no'

    print(result)


