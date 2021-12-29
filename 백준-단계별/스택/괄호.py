import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]

for tmp in arr:
    stack = []
    result = 'YES'
    for j in tmp:

        ## 이유는 모르겠지만 제일 마지막에 \n이 항상 붙어있어서 얘를 때줘야 함
        if j == '\n':
            continue
        ## 여는 괄호면 스택에 추가
        if j == '(':
            stack.append(j)

        else:
            ## 스택이 비어있을 때 닫는 괄호를 추가할 수 없음
            if not stack:
                result = 'NO'
                break
            ## 스택에 여는 괄호가 들어있다면 여는 괄호 하나를 지워주기
            else:
                stack.pop()

    ## 모든 괄호를 쳌했는데 스택에 무언가 남아있다면 그것은 No
    if stack:
        result = 'NO'
    print(result)


