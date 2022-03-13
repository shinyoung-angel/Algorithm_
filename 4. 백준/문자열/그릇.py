import sys
input = sys.stdin.readline

stack = list(input().strip())
answer = 0

for i in range(len(stack)):
    if i == 0:
        answer += 10
    elif stack[i] == stack[i-1]:
        answer += 5
    else:
        answer += 10

print(answer)
