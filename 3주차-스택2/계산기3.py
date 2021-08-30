
for tc in range(1, 11):
    N = int(input())
    TC = list(input())

    stack = []   # 연산자를 담고 계산할 것임
    num = []     # 후위표현식을 담을 것

    operator = {'(': 0, ')': 0, '-': 1, '+': 1, '*': 2, '/': 2}

    for i in TC:

        if i.isdigit():   # 요소가 숫자라면 num에다 추가
            num.append(i)

        elif i == '(':   # 요소가 열린 괄호라면 stack에 추가
            stack.append(i)

        elif i == ')':      # 닫힌 괄호가 나왔다면 열린 괄호가 나오기 전까지 요소들을 pop해서 후위표현식에 더해야 함
            while stack[-1] != '(':
                num.append(stack.pop())
            stack.pop()  # 열린 괄호는 pop해서 제거하기

        elif stack and operator[i] < operator[stack[-1]]:  # 연산자의 우선순위가 작다면 pop을 하다가 현재 연산자의 우선순위가 높아졌다면 멈춰!! pop하지 않음
            while stack and operator[i] < operator[stack[-1]] :  # 현재 쟤가 더 커? 멈춰  반대로 생각하려무나
                num.append(stack.pop())
            stack.append(i)

        elif stack and operator[i] == operator[stack[-1]]:  # 연산자의 우선순위가 같을 때도 고려해줘야 함. 우선순위가 같지 않을 때까지 pop하고 멈춰!
            while stack and operator[i] == operator[stack[-1]] : # 헷갈림,,, 둘이 같지 않아? 멈춰!
                num.append(stack.pop())
            stack.append(i)

        else:
            stack.append(i)   # 스택의 마지막 아이보다 연산자 우선순위가 높다면 stack에 push

    while stack:
        num.append(stack.pop())  # stack에 남아 있는 모든 아이들을 후위표현식에 마저 푸쉬

    for i in num:
        if i.isdigit():
            stack.append(i)   # 현재 stack은 비어 있으니 숫자라면 숫자를 넣어 줌.

        else:

            b = int(stack.pop())
            a = int(stack.pop())

            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a//b)

    print('#{} {}'.format(tc, stack.pop()))
