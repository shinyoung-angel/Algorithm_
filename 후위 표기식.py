import sys
input = sys.stdin.readline

priority = {'(': 1, '+': 2, '-': 2, '*':3, '/': 3}

test_case = input()
stack = []
result = ''

for i in test_case:

    if i == '(': stack.append(i)

    elif i.isalpha(): result += i

    elif i in ['+', '-', '/', '*']:
        if not stack or priority[stack[-1]] < priority[i]:
            stack.append(i)
        else:
            while stack:
                if priority[stack[-1]] >= priority[i]:
                    result += stack.pop()
                else:
                     break
            stack.append(i)

    elif i == ')':
        while stack:
            if stack[-1] != '(':
                result += stack.pop()
            else:
                break
        stack.pop()

while stack:
    result += stack.pop()

print(result)

