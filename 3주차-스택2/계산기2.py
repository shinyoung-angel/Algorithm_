for tc in range(1, 11):
    N = int(input())
    infix = input()
    stack = []
    postfix = []

    op = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}

    for inf in infix:
        if inf.isdigit():  # 숫자는 그냥 출력
            postfix += inf
            continue

        if inf == "(":  # 우선순위 최하위인 여는 괄호는 그냥 push
            stack.append("(")

        elif inf == ")":  # 닫는 괄호는 여는 괄호가 나올 때 까지 pop
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()

        elif stack and op[inf] < op[stack[-1]]:  # 스택이 있는데 top 보다 우선순위가 낮다면
            while stack and op[inf] < op[stack[-1]]:  # 그렇지 않을때까지 pop
                postfix += stack.pop()
            stack.append(inf)

        else:  # 스택이 비었거나, 우선순위가 높은 연산자면 그냥 push
            stack.append(inf)

    while stack:
        postfix += stack.pop()

    for pof in postfix:
        if pof in "0123456789":  # 숫자는 그냥 push
            stack.append(pof)
            continue

        else:  # -, / 연산은 순서가 상관없으므로 역순으로 연산
            temp_b = int(stack.pop())
            temp_a = int(stack.pop())
            if pof == "+":
                stack.append(temp_a + temp_b)
            elif pof == "*":
                stack.append(temp_a * temp_b)
            elif pof == "-":
                stack.append(temp_a - temp_b)
            elif pof == "/":
                stack.append(temp_a / temp_b)

    print("#{} {}".format(tc, stack.pop()))