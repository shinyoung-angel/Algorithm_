
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    max_school = 'me'
    max_alchol = 0
    for _ in range(n):
        a, b = input().split()
        if int(b) > max_alchol:
            max_school = a
            max_alchol = int(b)

    print(max_school)