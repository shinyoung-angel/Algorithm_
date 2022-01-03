import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
tmp = True
stack = []
result = []

for i in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        tmp = False
        break

if tmp == False:
    print('NO')
else:
    for i in result:
        print(i)