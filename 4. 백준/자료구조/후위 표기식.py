import sys
input = sys.stdin.readline

## 후위 표기식 문제
## 괄호와 연산자에 우선순위를 줌
priority = {'(': 1, '+': 2, '-': 2, '*':3, '/': 3}

test_case = input()
stack = []
result = ''

for i in test_case:

    if i == '(': stack.append(i)    ## (는 바로 스택에 넣기

    elif i.isalpha(): result += i   ## 알파벳은 result에 바로 넣기

    elif i in ['+', '-', '/', '*']:
        if not stack or priority[stack[-1]] < priority[i]: ## 스택이 비었거나 제일 마지막 연산자의 우선순위가 나보다 낮다면 스택에 바로 추가
            stack.append(i)
        else:
            while stack:
                if priority[stack[-1]] >= priority[i]:      ## 그것이 아니라면 나의 우선순위가 젤 높을 때까지 pop해서 result에 추가
                    result += stack.pop()
                else:
                     break
            stack.append(i)             ## 이후 현재의 연산자를 스택에 넣기

    elif i == ')':                      ## 닫느 괄호는 여는 괄호를 만날 때까지 스택을 pop하고 result에 추가 함
        while stack:
            if stack[-1] != '(':
                result += stack.pop()
            else:
                break
        stack.pop()                 ## 여는 괄호 pop

while stack:                        ## 스택에 남아 있는 요소를 마저 result에 넣어줌
    result += stack.pop()

print(result)

