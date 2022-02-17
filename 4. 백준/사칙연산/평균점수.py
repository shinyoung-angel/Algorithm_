import sys
input = sys.stdin.readline

result = []

for i in range(5):
    tmp = int(input())
    if tmp < 40:
        tmp = 40
    result.append(tmp)

print(int(sum(result)/5))