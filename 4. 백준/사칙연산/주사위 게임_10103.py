import sys
input = sys.stdin.readline


chang = 100
sang = 100

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        sang -= a
    elif a < b:
        chang -= b
    else:
        continue

print(chang)
print(sang)
