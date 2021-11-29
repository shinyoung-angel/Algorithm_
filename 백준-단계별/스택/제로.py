import sys
input = sys.stdin.readline

k = int(input())
stack = [0]

for i in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))